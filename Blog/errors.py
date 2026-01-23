from django.http import JsonResponse

def custom_404(request, exception):
    return JsonResponse({"error":"The requested endpoint was not found!"}, status=404)

def custom_500(request):
    return JsonResponse({"error":"A server error occured!"}, status=500)


"""
Custom_404 handles serving valid JSON responses when a URL is not found.
Custom_500 handles serving valid JSON responses when a server error occurs.
"""