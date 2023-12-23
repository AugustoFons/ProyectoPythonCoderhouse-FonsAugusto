from django.shortcuts import render, get_object_or_404, redirect
from carreras.models import Carrera, Comision, Alumno, Suscripto
from django.db.models import Count
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def carreras(request):
    if request.method == 'POST':
        #suscripcion
        if 'email' in request.POST:
            nuevo_suscriptor = Suscripto(suscripto=request.POST["email"])
            nuevo_suscriptor.save()
            return redirect('/')
        #busqueda
        elif 'nombre' in request.POST:
            data = request.POST.get("nombre", "")
            lista_busq = Carrera.objects.filter(nombre=data)
            carreras = Carrera.objects.all()  # Obtener todas las carreras para el select
            return render(request, 'pages/index.html', {'lista': lista_busq, 'carreras': carreras})
    else:
        carreras = Carrera.objects.all()
        return render(request, 'pages/index.html', {'carreras': carreras})


def info_carrera(request, carrera_id):
    carrera = get_object_or_404(Carrera, id=carrera_id)
    comisiones = Comision.objects.filter(carrera=carrera)

    return render(request, 'pages/info_carrera.html', {'carrera_info': carrera, 'comisiones': comisiones})

@login_required(login_url="login")
def inscribirse(request):
    carrera_nombre = request.GET.get('carrera_nombre')
    comisiones = Comision.objects.annotate(num_alumnos=Count('Alumnos')).filter(carrera__nombre=carrera_nombre, num_alumnos__lt=20)
    carreras = Carrera.objects.all()

    if request.method == "POST":
        nuevo_alumno = Alumno(
            carrera_id=request.POST["carrera_nombre"],
            nombre=request.POST["nombre"],
            dni=request.POST["dni"],
            comision_id=request.POST["comision"],
            email=request.POST["email"]
        )
        nuevo_alumno.save()
        return redirect('/')
    
    return render(request, 'pages/inscripcion.html', {'comisiones': comisiones, 'carreras': carreras})

def lista_alumnos(request):
    codigo_comision = request.GET.get('codigo_comision')
    alumnos = Alumno.objects.filter(comision__codigo=codigo_comision)
    cantidad_alumnos = alumnos.count()

    return render(request, 'pages/lista_alumnos.html', {
        'alumnos': alumnos,
        'codigo_comision': codigo_comision,
        'cantidad_alumnos': cantidad_alumnos,
    })

#####CRUD CARRERAS#####
def crear_carrera(request):
    if request.method == "POST":
        nueva_carrera = Carrera(
            nombre = request.POST["nombre"],    #entre comillas va el name del form
            duracion = request.POST["duracion"],
            descripcion = request.POST["descripcion"],
            url_img = request.POST["url_img"],
            categoria = request.POST["categoria"]
        )
        nueva_carrera.save()
        return redirect('/')

    return render(request, 'pages/crear_carrera.html')

def editar_carrera(request, nombre_carrera):
    carrera= Carrera.objects.get(nombre=nombre_carrera)

    if request.method == 'POST':
        carrera.nombre= request.POST["nombre"]
        carrera.duracion = request.POST["duracion"]
        carrera.descripcion = request.POST["descripcion"]
        carrera.url_img = request.POST["url_img"]
        carrera.categoria = request.POST["categoria"]

        carrera.save()
        return redirect('/')
    
    return render(request, 'pages/editar_carrera.html', {'carrera': carrera})

def eliminar_carrera(request, nombre_carrera):
    carrera= Carrera.objects.get(nombre=nombre_carrera)
    carrera.delete()
    return redirect('/')

#####CRUD COMISION#####
def crear_comision(request):
    carreras= Carrera.objects.all()
    if request.method == "POST":
        nueva_comision = Comision(
            carrera_id = request.POST["carrera"],    #entre comillas va el name del form
            codigo = request.POST["codigo"],
            horario = request.POST["horario"],
            fecha = request.POST["fecha"],
        )
        nueva_comision.save()
        return redirect('/')

    return render(request, 'pages/crear_comision.html', {'carreras': carreras})

def editar_comision(request, codigo_comision):
    comision= Comision.objects.get(codigo=codigo_comision)
    carreras= Carrera.objects.all()

    if request.method == 'POST':
        comision.carrera_id = request.POST["carrera"]
        comision.codigo = request.POST["codigo"]
        comision.horario = request.POST["horario"]
        comision.fecha = request.POST["fecha"]

        comision.save()
        return redirect('/')
    
    return render(request, 'pages/editar_comision.html', {'comision': comision, 'carreras': carreras})

def eliminar_comision(request, codigo_comision):
    comision= Comision.objects.get(codigo=codigo_comision)
    comision.delete()
    return redirect('/')

###Eliminar Alumno###
def eliminar_alumno(request, alumno_id):
    alumno = Alumno.objects.get(pk=alumno_id)
    alumno.delete()
    return redirect('/')
