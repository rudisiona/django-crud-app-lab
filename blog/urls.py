from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('blogs/', views.index, name='index'),
    # path("", views.index, name="index"),
]
