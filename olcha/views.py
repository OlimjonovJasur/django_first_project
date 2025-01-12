from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    # request: GET, POST, PUT, PATCH, DELETE
    html_content = """
    <h1>Assalomu aleykum</h1>
    <h2>Mening ismim Jasur</h2>
    <h3>Men Namangandanman, 2004 - yilman</h3>
    <h4>Men TATU talabasiman</h4>
    <h5>qiziqishlarim futbol, pls, tennis, kitob o'qish</h5>
    <p>Hurmatli do'stlar bu mening birinchi django web dasturim
    """
    return HttpResponse(html_content)