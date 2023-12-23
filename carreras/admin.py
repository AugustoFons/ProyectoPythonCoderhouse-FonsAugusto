from django.contrib import admin

# Register your models here.
from carreras.models import Comision, Carrera, Alumno, Suscripto
# Register your models here.

admin.site.register(Carrera)
admin.site.register(Comision)
admin.site.register(Alumno)
admin.site.register(Suscripto)
