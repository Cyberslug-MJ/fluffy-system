from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.exceptions import NotFound

class MyCustomPagination(PageNumberPagination):
    page_size_query_param = 'limit'

    def get_paginated_response(self, data):
        totalPages = self.page.paginator.num_pages
        currentPage = self.page.number
        totalItems = self.page.paginator.count
        hasMore = currentPage < totalPages

        if totalItems > 0:
            message = "Successful"
        else:
            message = "No data was found"

        return Response({
            'pagination': {
                'totalItems': totalItems,
                'limit': self.get_page_size(self.request),
                'currentPage': currentPage,
                'totalPages': totalPages,
                'hasMore': hasMore,
                'nextPage': currentPage + 1 if self.get_next_link() else None,
                'previousPage': currentPage - 1 if self.get_previous_link() else None,
            },
            'data': data,
            'message': message
        })
    
    
    def paginate_queryset(self, queryset, request, view=None):
        try:
            return super().paginate_queryset(queryset, request, view=view)
        except NotFound:
            # Reset to page 1 if page is out of range
            request.query_params._mutable = True  # only if using QueryDict
            request.query_params['page'] = 1
            return super().paginate_queryset(queryset, request, view=view)


def paginate_my_way(queryset,request,serializer,order='pk'):
    paginator = MyCustomPagination()
    paginator.page_size = 10
    paginated_queryset = paginator.paginate_queryset(queryset.order_by(order),request)
    serializer = serializer(paginated_queryset,many=True)
    return paginator.get_paginated_response(serializer.data)