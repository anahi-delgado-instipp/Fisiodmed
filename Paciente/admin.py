from django.contrib import admin
from .models import Especialidad, Pacientes, Medicos

# Register your models here.

admin.site.register(Pacientes)
admin.site.register(Especialidad)
admin.site.register(Medicos)
