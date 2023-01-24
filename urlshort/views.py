from django.shortcuts import render

from .models import ShortURL


def home(request):
    return render(request, 'urlshort/home.html')

def redirect(request, url):
    current_obj = ShortURL.objects.filter(short_url=url)
    if len(current_obj) == 0:
        return render(request, 'urlshort/pagenotfound.html')
    context = {
        'obj':current_obj[0],
    }
    return render(request, 'urlshort/redirect.html', context)

def createShortURL(request):
    pass














