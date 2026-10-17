from django.urls import path
from pages import views

urlpatterns = [
    # Cada ruta apunta a la vista 'page' enviándole el slug exacto que le corresponde
    path('hola-adso/', views.page, {'slug': 'hola-adso'}, name="hola_adso"),
    path('trabaja-con-nosotros/', views.page, {'slug': 'trabaja-con-nosotros'}, name="trabaja"),
    path('servicios/', views.page, {'slug': 'servicios'}, name="servicios"),
    path('sobre-nosotros/', views.page, {'slug': 'sobre-nosotros'}, name="sobre_nosotros"),
    
    # Ruta genérica por si agregas más páginas mediante slug
    path('<str:slug>/', views.page, name="page"),
]