from django.shortcuts import render
from movieapp.models import Category,Movielist
from django.db.models import Q
from django.contrib import messages
# Create your views here.


def searchresult(req):
    search_movies=None
    query=None
    if 'q' in req.GET:
        query = req.GET.get('q')
        search_movies = Movielist.objects.filter(Q(name__contains=query) | Q(desc__contains=query))
        return render(req,'search.html',{'query':query,'search_movies':search_movies})