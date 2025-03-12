from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

class WatchlistPagination(PageNumberPagination):
    page_size = 2
    page_query_param="p"
    page_size_query_param = 'page_size'
    max_page_size=10  #limit of element per page
    last_page_strings = "end"
    

class WatchlistLOPagination(LimitOffsetPagination):
    default_limit = 5
    limit_query_param='limit'
    offset_query_param='start'
    max_limit = 10