from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_book, name='posts'),
    path('posts/<int:id>/', views.detail_book, name='detail'),
    path('add_book/', views.add_post, name='add_book')
]
