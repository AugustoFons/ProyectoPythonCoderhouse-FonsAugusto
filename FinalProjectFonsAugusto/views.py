from django.shortcuts import render, redirect

#obtener productos
def home(request):
    return render(request,  'pages/base.html')
