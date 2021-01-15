from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView, ListView, TemplateView
from .models import Pizza


class PizzasIndexView(ListView):
    template_name = 'pizzas/index.html'
    context_object_name = 'pizzas'
    paginate_by = 2
    def get_queryset(self):
        q = self.request.GET.get('q')
        if q and q != '':
            return Pizza.objects.filter(name__icontains=q)
        else:
            return Pizza.objects.all()
    
    
class PizzaDetailView(DetailView):
    model = Pizza
    context_object_name = 'pizza'    
    

class PizzaCreateView(PermissionRequiredMixin, 
                      SuccessMessageMixin,
                      CreateView):
    model = Pizza
    fields = ['name', 'price', 'toppings', 'image']    
    action = 'Add pizza'
    success_url = reverse_lazy('pages:home')
    permission_required = 'pizzas.add_pizza'
    success_message = '"%(name)s" was created successfully'


class PizzaUpdateView(PermissionRequiredMixin, UpdateView):
    model = Pizza
    fields = ['name', 'price', 'toppings', 'image']
    action = 'Edit pizza'
    success_url = reverse_lazy('pages:home')
    permission_required = 'pizzas.change_pizza'
     

class PizzaDeleteView(PermissionRequiredMixin, DeleteView):
    model = Pizza
    success_url = reverse_lazy('pages:home')
    permission_required = 'pizzas.delete_pizza'
    



