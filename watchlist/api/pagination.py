from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class WatchListPagination(PageNumberPagination):

    page_size = 7
    page_size_query_param = 'size'
    max_page_size = 11


class WatchListLOPagination(LimitOffsetPagination):

    default_limit = 5
    offset_query_param = 'start'
    max_limit = 10
