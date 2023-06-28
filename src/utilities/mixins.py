import json
import redis
import requests

from abc import ABC, abstractmethod


class AbstractHttpBase(ABC):
    """
    Abstract class which help child classes make http calls.
    Child classes must declare properties:
        - base_url: Base url of Application/Service
        - header: Header to pass in HTTP Requests
        - paths: relative path of urls
    """

    @property
    @abstractmethod
    def base_url(self):
        pass

    @property
    @abstractmethod
    def header(self):
        pass

    @property
    @abstractmethod
    def paths(self):
        pass

    @property
    def __method_dispatcher(self):
        return {
            "get": requests.get,
            "post": requests.post,
            "put": requests.put,
            "delete": requests.delete,
            "patch": requests.patch,
            "head": requests.head,
        }

    def get_status_and_response(self, path, data={}, headers={}, method="get"):
        method = self.__method_dispatcher.get(method.lower())
        assert method, f"{method} not found"

        if not headers:
            headers = self.header

        url = f"{self.base_url}{path}"
        response = method(url, data=data, headers=headers)
        return response.status_code, response.json()


class AbstractCacheBase(ABC):
    """
    Abstract class which help child classes store & retrieve data to & from redis cache.
    Child classes must declare properties:
        - cache_prefix: Prefix to be used with all cache keys
        - cache_timeout: a datetime.timedelta field after which keys should expire
    """

    @property
    @abstractmethod
    def cache_prefix(self):
        pass

    @property
    @abstractmethod
    def cache_timeout(self):
        pass

    def cache_lookup(self, key):
        return self.cache.get(f"{self.cache_prefix}_{key}")

    def set_cache(self, key, value):
        self.cache.setex(f"{self.cache_prefix}_{key}", self.cache_timeout, value)

    def __init__(self, *args, **kwargs):
        self.cache = redis.Redis()
        super().__init__(*args, **kwargs)
