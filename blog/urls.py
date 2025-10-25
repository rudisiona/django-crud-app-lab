from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.base, name='base'),
    path('home/', views.Home.as_view(), name='home'),
    path('blogs/', views.index, name='index'),
    path('create/', views.Create.as_view(), name='create'),
    path('blogs/<int:blog_id>/', views.blog_detail, name='blog-detail'),
    path('blogs/<int:pk>/update/', views.Update.as_view(), name='blog-update'),
    path('blogs/<int:pk>/delete/', views.Delete.as_view(), name='blog-delete'),
    path('signup/', views.signup, name='signup'),
    # path("", views.index, name="index"),
]
