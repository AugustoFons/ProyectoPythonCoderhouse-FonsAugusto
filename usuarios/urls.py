from django.urls import path
from usuarios.views import registro, login_request, Logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', login_request, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('registro/', registro, name='registro'),
]