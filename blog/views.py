from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from .models import Blog
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect


# Create your views here.

# class Blog: 
#     def __init__(self, title, post, date):
#         self.title = title
#         self.post = post
#         self.date = datetime.now()

blogs = [
    Blog('1', '1', datetime(2025, 10, 21)),
    Blog('2', '2', datetime(2025, 10, 21)),
    Blog('3', '3', datetime(2025, 10,20)),
]    

class Create(CreateView):
    model = Blog
    fields= ['title', 'post']
    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class Update(UpdateView):
    model = Blog
    fields = ['title', 'post']

class Delete(DeleteView):
    model = Blog
    success_url = '/blogs/'
        
class Home(LoginView):
    template_name = 'blog/login.html'


def base(request):
    return render(request, 'blog/home.html')


def index(request):
    blogs = Blog.objects.filter(user=request.user)
    # blogs = request.user.blog_set.all()
    return render(request, 'blogs/index.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blogs/detail.html', {'blog': blog})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
   