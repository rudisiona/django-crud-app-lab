from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

class Blog: 
    def __init__(self, title, post, date):
        self.title = title
        self.post = post
        self.date = datetime.now()

blogs = [
    Blog('1', '1', datetime(2025, 10, 21)),
    Blog('2', '2', datetime(2025, 10, 21)),
    Blog('3', '3', datetime(2025, 10,20)),
]    

def base(request):
    return HttpResponse('welcome home')

def home(request):
    return render(request, 'blogs/home.html')

def index(request):
    return render(request, 'blogs/index.html', {'blogs': blogs})