from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_book, name='posts'),
    path('posts/<int:id>/', views.detail_book, name='detail'),
    path('posts/<int:id>/update', views.update_book, name='update'),
    path('posts/<int:id>/delete', views.delete_book, name='delete'),
    path('add_book/', views.add_post, name='add_book')
]
