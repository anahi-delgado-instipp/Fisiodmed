
from django.contrib import admin
from django.urls import path
from Paciente import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    #SISTEMA
    path('base/', views.base_view, name='base'),
    path('login/', views.login_view, name='login'),
    path('inicio/', views.inicio_view, name='inicio'),
    path('especialidades/', views.especialidades_view, name='especialidades'),
    path('contactos/', views.contactos_view, name='contactos'),
    path('registrar/', views.registrar_view, name='registrar'),
    path('logout/', views.logout_view, name='logout'),

    #PACIENTE

    path('ListadoPaciente/', views.ListadoPaciente_view, name='ListadoPaciente'),
    path('editarpaciente/<int:id>/', views.editarpaciente_view, name='editarpaciente'),
    path('eliminarpaciente/<int:id>/', views.eliminarpaciente_view, name='eliminarpaciente'),
    path('registropaciente/', views.registropaciente_view, name='registropaciente'),

    #MEDICOS
    path('ListadoMedico/', views.ListadoMedico_view, name='ListadoMedico'),
    path('registrarmedico/', views.registrarmedico_view, name='registrarmedico'),
    path('editarmedico/<int:id>/', views.editarmedico_view, name='editarmedico'),
    path('eliminarmedico/<int:id>/', views.eliminarmedico_view, name ='eliminarmedico'),

    #CITAS
    path('agendarcita/', views.agendarcita_view, name='agendarcita'),
    path('registrarcita/', views.registrarcita_view, name='registrarcita'),
    path('editarcitas/<int:id>/', views.editarcita_view, name='editarcitas'),
    path('eliminarcita/<int:id>/', views.eliminarcita_view, name='eliminarcita'),

    #ESPECIALIDADES
    path('registroespecialidad/', views.registroespecialidad_view, name='registroespecialidad'),
    path('listarespecialidad/', views.Listarespecialidad_view, name='listarespecialidad'),
    path('editarespecialidad/<int:id>/', views.editarespecialidad_view, name='editarespecialidad'),
    path('eliminarespecialidad/<int:id>/', views.eliminarspecialidad_view, name='eliminarespecialidad'),


]
