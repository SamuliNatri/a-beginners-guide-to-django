from django.urls import path
from . import views

app_name = 'pizzas'

urlpatterns = [
    path('', 
         views.PizzasIndexView.as_view(), 
         name='index'),
    path('add/', 
         views.PizzaCreateView.as_view(), 
         name='add'),
    path('<slug:slug>/', 
         views.PizzaDetailView.as_view(),
         name='detail'),
    path('<int:pk>/update/', 
         views.PizzaUpdateView.as_view(), 
         name='update'),
    path('<int:pk>/delete/', 
         views.PizzaDeleteView.as_view(), 
         name='delete'),
]