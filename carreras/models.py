from django.db import models

# Create your models here.
class Carrera(models.Model):
    nombre= models.CharField(max_length=100)
    duracion= models.IntegerField(default=0)
    descripcion= models.TextField()
    url_img= models.TextField()
    categoria= models.CharField(max_length=120, default='')
    def __str__(self):
        return self.nombre
    
class Comision(models.Model):
    carrera= models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name="comisiones")
    codigo = models.CharField(max_length=30, default='')
    horario= models.CharField(max_length=30, default='')
    fecha= models.CharField(max_length=60)

    def __str__(self):
        return self.codigo

class Alumno(models.Model):
    carrera= models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name="Alumnos")
    comision= models.ForeignKey(Comision, on_delete=models.CASCADE, related_name="Alumnos")
    nombre= models.CharField(max_length=70)
    dni= models.CharField(max_length=20, default='')
    email= models.EmailField(default='alumno@gmail.com')

    def __str__(self):
        return self.nombre

class Suscripto(models.Model):
    suscripto= models.EmailField(default= 'alumno@gmail.com')

    def __str__(self):
        return self.suscripto