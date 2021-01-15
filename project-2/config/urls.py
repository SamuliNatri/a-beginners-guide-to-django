from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('pizzeria.pages.urls')),
    path('pizzas/', include('pizzeria.pizzas.urls')),
    path('feedback/', include('pizzeria.feedback.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), 
] + static(settings.MEDIA_URL, 
           document_root=settings.MEDIA_ROOT)
