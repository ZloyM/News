from django.shortcuts import render
from .models import New


# Create your views here.
def default(request):
    return render(request, 'default.html')


def news(request):
    news = New.objects.all()
    return render(request, 'news.html', context={'news': news})


def detail(request, slug):
    new = New.objects.get(slug__iexact=slug)
    return render(request, 'details.html', context={'new': new})