from django.shortcuts import render, get_object_or_404
from django.contrib import messages

def handler404(request, exception):
    response = render(request, "templates/404.html")
    response.status_code = 404
    return response
