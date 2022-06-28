"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('edificio/<int:id>', views.obtener_edificio, 
            name='obtener_edficio'),
        path('crear/edificio', views.crear_edficio, 
            name='crear_edificio'),
        path('editar_edificio/<int:id>', views.editar_edificio, 
            name='editar_edificio'),
        path('eliminar/edficio/<int:id>', views.eliminar_edficio, 
            name='eliminar_edificio'),
        # Edificios
        path('crear/departamento', views.crear_departamento, 
            name='crear_departamento'),
        path('editar/departamento/<int:id>', views.editar_departamento, 
            name='editar_departamento'),
        path('crear/departamento/edificio/<int:id>', 
            views.crear_departamento_edificio, 
            name='crear_departamento_estudiante'),
 ]
