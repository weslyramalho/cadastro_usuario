
from django.urls import path
from app_cad_usuario import views

urlpatterns = [
    # rota, view responsavel, nome de referencia
    path('', views.home,name='home'),
]
