from pizzeria.pizzas.models import Pizza


def pizzas_total(request):
    return {
        'pizzas_total': Pizza.objects.count()
        }