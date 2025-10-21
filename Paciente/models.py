from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   telefono = models.CharField(max_length=15, blank=True, null=True)
   fecha_nacimiento = models.DateField(blank=True, null=True)
   direccion = models.CharField(max_length=255, blank=True, null=True)
   cedula = models.CharField(max_length=15, blank=True, null=True)

   def __str__(self):
        return f"{self.user.username}'s profile"

class Pacientes(models.Model):
    nombres = models.CharField(max_length=225)
    apellidos = models.CharField(max_length=225)
    cedula = models.CharField(max_length=15)
    direccion = models.CharField(max_length=225)
    celular = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField(verbose_name='fecha_nacimiento')
    edad = models.IntegerField()
    estado_civil = models.CharField(max_length=28, verbose_name='estado civil')
    tipo_sangre = models.CharField(max_length=3, null=True, verbose_name='tipo de sangre')
    apellido_espos = models.CharField(max_length=225)
    canton = models.CharField(max_length=1000)
    correo =models.EmailField(null=True)
    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

from django.db import models

class Especialidad(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Citas(models.Model):
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    fecha_cita = models.DateField(verbose_name='fecha de la cita')
    hora_cita = models.TimeField(verbose_name='hora de la cita')
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, default=1)
    medico = models.ForeignKey('Medicos', on_delete=models.CASCADE, verbose_name='Médico')
    def __str__(self):
        return f"Cita con {self.paciente} el {self.fecha_cita} a las {self.hora_cita}"


class Medicos(models.Model):
    nombres = models.CharField(max_length=225)
    apellidos = models.CharField(max_length=225)
    cedula = models.CharField(max_length=15)
    direccion = models.CharField(max_length=225)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"





