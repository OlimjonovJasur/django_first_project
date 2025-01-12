from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    # request: GET, POST, PUT, PATCH, DELETE
    html_content = """
    <h1>Assalomu aleykum</h1>
    <p>Hurmatli do'stlar bu mening birinchi django web dasturim
    """
    return HttpResponse(html_content)