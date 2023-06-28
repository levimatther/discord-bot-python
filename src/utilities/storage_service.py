from . import session
from .misc import singleton
from .models import SearchHistory


@singleton
class SearchHistoryService:
    """
    Service used to deal with data of user's Search History
    """

    def __init__(self):
        self.session = session

    def insert_search_history(self, user_id, term):
        instance = SearchHistory(user_id, term)
        self.session.add(instance)
        self.session.commit()

    def get_recent_related_searches(self, user_id, term, count=5):
        records = (
            self.session.query(SearchHistory)
            .filter(
                SearchHistory.search_term.like(f"%{term}%"),
                SearchHistory.user_id == user_id,
            )
            .order_by(SearchHistory.timestamp.desc())
            .limit(count)
        )
        return records
