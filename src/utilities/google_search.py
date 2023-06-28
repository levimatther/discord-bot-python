import os

import json
import datetime

from .constants import GOOGLE_SEARCH_CACHE_TIMEOUT
from .mixins import AbstractCacheBase, AbstractHttpBase


class GoogleSearch(AbstractHttpBase, AbstractCacheBase):
    """
    Performs google search and stores the response in cache
    """

    @property
    def api_key(self):
        return os.getenv("GOOGLE_SEARCH_API_KEY")

    @property
    def cx(self):
        return os.getenv("GOOGLE_SEARCH_CX")

    @property
    def base_url(self):
        return "https://www.googleapis.com"

    @property
    def cache_prefix(self):
        return "google_search"

    @property
    def cache_timeout(self):
        return GOOGLE_SEARCH_CACHE_TIMEOUT

    @property
    def header(self):
        return {}

    @property
    def paths(self):
        return {
            "CUSTOM_SEARCH_V1": "/customsearch/v1?key={GOOGLE_API_KEY}&cx={SEARCH_ENGINE_ID}&q={SEARCH_TERM}",
        }

    def get_top_five_links(self, search_term):
        """
        Looks for `search_term` into cache.
        If found:
            returns result from cache,
        Else:
            Search using Google's Search API and prepare, cache and return result

        NOTE/TODO: This method is breaking the open close principle by fetching top five results only.
        To avoid doing so, we'll have to dig deep into the google's api for paginated responses
        and create suitable `cx` as well.
        """
        if response := self.cache_lookup(search_term):
            return json.loads(response)

        status_code, response_json = self.get_status_and_response(
            self.paths["CUSTOM_SEARCH_V1"].format(
                GOOGLE_API_KEY=self.api_key,
                SEARCH_ENGINE_ID=self.cx,
                SEARCH_TERM=search_term,
            )
        )

        if status_code == 200:
            search_result_items = response_json.get("items", [])[0:5]
            response_to_return = []
            for search_result_item in search_result_items:
                response_to_return.append(
                    {
                        "title": search_result_item.get("title"),
                        "url": search_result_item.get("link"),
                    }
                )

            self.set_cache(search_term, json.dumps(response_to_return))
            return response_to_return
