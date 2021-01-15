from django.urls import path
from . import views

app_name = 'feedback'

urlpatterns = [
    path('add/', 
         views.feedback_add, 
         name='add'),
    path('<int:pk>/edit/', 
         views.feedback_edit, 
         name='edit'),
    path('<int:pk>/delete/', 
         views.feedback_delete, 
         name='delete'),
]