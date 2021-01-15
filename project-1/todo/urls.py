from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.detail, name='detail'),
    path('todo/add/', views.add, name='add'),
    path('todo/<int:pk>/edit/', views.edit, name='edit'),
    path('todo/<int:pk>/delete/', views.delete, name='delete'),
]