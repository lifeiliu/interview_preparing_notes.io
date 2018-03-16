from urllib import urlencode
from collections import OrderedDict

from constant import (
    SearchArticleTime,
    SearchArticleType
)

_search_official_account = 1
_search_article = 2


class SogouRequest:

    def __init__(self):
        pass

    @classmethod
    def generate_search_official_account_url(cls, keyword, page = 1):
        assert isinstance(page, int) and page > 0

        query = OrderedDict()
        query['type'] = _search_official_account
        query['page'] = page
        query['ie'] = 'utf8'
        query['query'] = keyword

        return 'http://weixin.sogou.com/weixin?%s.html' % urlencode(query)


    @classmethod
    def generate_search_article(cls, keyword, page, time = SearchArticleTime.ANYTIME,
                                article_type = SearchArticleType.ALL):
        assert isinstance(page, int) and page > 0

        query = OrderedDict()
        query['type'] = _search_article
        query['page'] = page
        query['ie'] = 'utf8'
        query['tsn'] = time
        query['query'] = keyword

        if article_type == SearchArticleType.ALL:
            query['interation'] = '%s,%s' % (SearchArticleType.IMAGE, SearchArticleType.VIDEO)
        else:
            query['interation'] = article_type

        return 'http://weixin.sogou.com/weixin?%s.html' % urlencode(query)
