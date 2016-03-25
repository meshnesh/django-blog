from django.http import HttpResponse
from django.shortcuts import render
from .models import PostLog

import requests

# Create your views here.
def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print r.text
    return HttpResponse('<pre>' + r.text + '</pre>')

def db(request):

    postlog = PostLog()
    postlog.save()

    postlogs = PostLog.objects.all()

    return render(request, 'db.html', {'postlogs': postlogs})