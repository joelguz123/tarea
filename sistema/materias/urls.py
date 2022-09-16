from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('materia', views.materia, name='materia'),
    path('materia/crear', views.crear, name='crear'),
    path('materia/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('materia/editar/<int:id>', views.editar, name='editar'),
    

    
]