from urllib import request
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Pacientes
from .models import Citas
from .models import Especialidad
from .models import Medicos
# Create your views here.

#SISTEMA 
def base_view(request):
    return render(request, 'base.html')

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'error':''
        })
    else:
       print (request.POST)
       user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
       print (user)
       if user is None:
           return render (request, 'login.html', {
               'error':'Usuario o contraseña incorrecta'
           })
       else:
           login(request, user)
           return render (request, 'inicio.html')

def logout_view(request):
    logout(request)
    return redirect('login')
             
@login_required
def inicio_view(request):
    return render(request, 'inicio.html')

@login_required
def registrar_view(request):
    return render(request, 'registrar.html')  

@login_required
def contactos_view(request):
    return render(request, 'contactos.html')




#################################################################################################################
#CITAS
@login_required
def agendarcita_view(request):
    citas = Citas.objects.all().order_by('-fecha_cita', '-hora_cita')
    return render(request, 'agendarcita.html', {'citas': citas})

#CRUD INSERTAR CITA 
@login_required
def registrarcita_view(request):
    if request.method == 'POST':
        paciente_id = request.POST['paciente']
        fecha = request.POST['fecha_cita']
        hora = request.POST['hora_cita']
        medico_id = request.POST['medico']
        especialidad_id = request.POST['especialidad']

        paciente = Pacientes.objects.get(id=paciente_id)
        medico = Medicos.objects.get(id=medico_id)
        especialidad = Especialidad.objects.get(id=especialidad_id)

        Citas.objects.create(
            paciente=paciente,
            fecha_cita=fecha,
            hora_cita=hora,
            medico=medico,
            especialidad=especialidad
        )
        return redirect('agendarcita')
    
    pacientes = Pacientes.objects.all()
    medicos = Medicos.objects.all()
    especialidades = Especialidad.objects.all()
    return render(request, 'registrarcita.html', {
        'pacientes': pacientes,
        'medicos': medicos,
        'especialidades': especialidades
    })

# CRUD CITAS EDITAR
@login_required

def editarcita_view(request, id):
    cita = get_object_or_404(Citas, pk=id)
    pacientes = Pacientes.objects.all()
    medicos = Medicos.objects.all()
    especialidades = Especialidad.objects.all()

    if request.method == 'POST':
        cita.paciente_id = request.POST['paciente']
        cita.fecha_cita = request.POST['fecha']
        cita.hora_cita = request.POST['hora']
        cita.medico_id = request.POST['medico']
        cita.especialidad_id = request.POST['especialidad']
        cita.save()
        return redirect('agendarcita') 

    return render(request, 'editarcitas.html', {
        'cita': cita,
        'pacientes': pacientes,
        'medicos': medicos,
        'especialidades': especialidades,
    })

#CRUD ELIMINAR CITA
def eliminarcita_view(request, id):
    cita = get_object_or_404(Citas, pk=id)
    cita.delete()
    return redirect('agendarcita')  # o donde quieras que vaya después de eliminar


@login_required
def especialidades_view(request):
    especialidades = Especialidad.objects.all()
    return render(request, 'especialidades.html', {'especialidades': especialidades})


#################################################################################################################
#PACIENTES

#CRUD LISTA 
@login_required
def ListadoPaciente_view(request):
    pacienteslistado = Pacientes.objects.all()
    return render(request, 'ListadoPaciente.html', {'pacientes': pacienteslistado})
#CRUD EDITAR 
@login_required
def editarpaciente_view(request, id):
    paciente = get_object_or_404(Pacientes, id=id)

    if request.method == 'POST':
        paciente.nombres = request.POST['nombres']
        paciente.apellidos = request.POST['apellidos']
        paciente.cedula = request.POST['cedula']
        paciente.direccion = request.POST['direccion']
        paciente.celular = request.POST['celular']
        paciente.fecha_nacimiento = request.POST['fecha_nacimiento']
        paciente.edad = request.POST['edad']
        paciente.estado_civil = request.POST['estado_civil']
        paciente.tipo_sangre = request.POST['tipo_sangre']
        paciente.apellido_espos = request.POST['apellido_espos']
        paciente.canton = request.POST['canton']
        paciente.correo = request.POST['correo']
        paciente.save()

        return redirect('ListadoPaciente')

    return render(request, 'editarpaciente.html', {'paciente': paciente})

#CRUD ELIMINAR 
@login_required
def eliminarpaciente_view(request, id):
    paciente = Pacientes.objects.get(id=id)
    paciente.delete()
    return redirect('ListadoPaciente')

# CRUD AGREGAR
@login_required
def registropaciente_view(request):
    if request.method == 'POST':
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        edad = request.POST['edad']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        direccion = request.POST['direccion']
        canton = request.POST['canton']
        estado_civil = request.POST['estado_civil']
        apellido_espos = request.POST['apellido_espos']
        correo = request.POST['correo']
        tipo_sangre = request.POST['tipo_sangre']
        celular = request.POST['celular']
        cedula = request.POST['cedula']

        Pacientes.objects.create(
            nombres=nombres,
            apellidos=apellidos,
            edad=edad,
            fecha_nacimiento=fecha_nacimiento,
            direccion=direccion,
            canton=canton,
            estado_civil=estado_civil,
            apellido_espos=apellido_espos,
            correo=correo,
            tipo_sangre=tipo_sangre,
            celular=celular,
            cedula=cedula
        )
        return redirect('ListadoPaciente') 
    return render(request, 'registropaciente.html')

#################################################################################################################
#ESPECIALIDAD
#CRUD LISTAR
@login_required
def Listarespecialidad_view(request):
    especialidades = Especialidad.objects.all()
    return render(request, 'listarespecialidad.html', {'especialidades': especialidades})

#CRUD AGREGAR
@login_required
def registroespecialidad_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        if nombre:
            Especialidad.objects.create(nombre=nombre)
            return redirect('listarespecialidad')
    return render(request, 'registrarespecialidades.html')

#CRUD EDITAR
@login_required
def editarespecialidad_view(request, id):
    especialidad = get_object_or_404(Especialidad, id=id)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        especialidad.nombre = nombre
        especialidad.save()
        return redirect('listarespecialidad')

    return render(request, 'editarespecialidad.html', {'especialidad': especialidad})
#CRUD ELIMINAR
@login_required
def eliminarspecialidad_view(request, id):
    especialidad = get_object_or_404(Especialidad, id=id)
    especialidad.delete()
    return redirect('listarespecialidad')

#################################################################################################################
#MEDICOS
# CRUD LISTAR
@login_required
def ListadoMedico_view(request):
    medicos = Medicos.objects.all()
    return render(request, 'ListadoMedico.html', {'medicolista': medicos}) 

# CRUD AGREGAR
@login_required
def registrarmedico_view(request):
    if request.method == 'POST':
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        cedula = request.POST['cedula']
        direccion = request.POST['direccion']
        
        Medicos.objects.create(
            nombres=nombres,
            apellidos=apellidos,
            direccion=direccion,
            cedula=cedula
        )
        return redirect('ListadoMedico')
    return render(request, 'registrarmedico.html')

# CRUD EDITAR
@login_required
def editarmedico_view(request, id):
    medico = get_object_or_404(Medicos, pk=id)

    if request.method == 'POST':
        medico.nombres = request.POST.get('nombres')
        medico.apellidos = request.POST.get('apellidos')
        medico.cedula = request.POST.get('cedula')
        medico.direccion = request.POST.get('direccion')
        medico.save()
        return redirect('ListadoMedico')  

    return render(request, 'editarmedico.html', {'medico': medico})
#CRUD ELIMINAR
@login_required
def eliminarmedico_view(request, id):
    medico = get_object_or_404(Medicos, id=id)
    medico.delete()
    return redirect('ListadoMedico')
