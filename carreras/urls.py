from django.urls import path
from . import views

urlpatterns = [
    # ...otras rutas
    path('<int:carrera_id>/', views.info_carrera, name='info_carrera'),
    path('inscribirse/', views.inscribirse, name='inscribirse'),
    path('comision/', views.lista_alumnos, name='ver_comision'),
    path('crear/', views.crear_carrera, name='crear'),
    path('editar/<nombre_carrera>/', views.editar_carrera, name="editar"),
    path('eliminar/<nombre_carrera>/', views.eliminar_carrera, name="eliminar"),
    path('crear_comision/', views.crear_comision, name="crear_comision"),
    path('editar_comision/<codigo_comision>/', views.editar_comision, name="editar_comision"),
    path('eliminar_comision/<codigo_comision>/', views.eliminar_comision, name="eliminar_comision"),
    path('carreras/eliminar_alumno/<int:alumno_id>/', views.eliminar_alumno, name='eliminar_alumno'),

]