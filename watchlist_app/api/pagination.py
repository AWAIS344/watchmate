from rest_framework.pagination import PageNumberPagination

class WatchlistPagination(PageNumberPagination):
    page_size = 2
    page_query_param="p"
    page_size_query_param = 'page_size'
    max_page_size=10  #limit of element per page
    last_page_strings = "end"
    