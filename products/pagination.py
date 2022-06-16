from rest_framework.pagination import LimitOffsetPagination

class CategoryLimitOffsetPagination(LimitOffsetPagination): 
    default_limit = 5

class ProductLimitOffsetPagination(LimitOffsetPagination): 
    default_limit = 5