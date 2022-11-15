from django.contrib import admin

# Register your models here.
from sistemaLicencia.models import Persona, Turno, Clave, Pregunta, Examen, Estadistica, Cuestionario

# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    list_display = ("dni", "nombre", "edad", "examenRendidos")
    search_fields = ("dni", "nombre")
    list_filter = ("anteojos",)

class TurnoAdmin(admin.ModelAdmin):
    list_display = ("idPersona", "nombreTurno", "fechaTurno")
    list_filter = ("fechaTurno",)

class ClaveAdmin(admin.ModelAdmin):
    list_display = ("clave", "idPersona", "fechaExamen", "tiempoLimite")
    list_filter = ("fechaExamen",)
    search_fields = ("clave", "idPersona")

class PreguntaAdmin(admin.ModelAdmin):
    list_display = ("idPregunta", "pregunta", "respuesta1", "respuesta2", "respuesta3", "respuesta4")
    search_fields = ("pregunta", "idPregunta")

class CuestionarioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "idPregunta")
    search_fields = ("nombre",)

class ExamenAdmin(admin.ModelAdmin):
    list_display = ("idExamen", "clave", "rendido", "preguntasCorrectas")
    search_fields = ("idExamen", "clave")
    list_filter = ("preguntasCorrectas",)

class EstadisticaAdmin(admin.ModelAdmin):
    list_display = ("rendido", "aprobado", "reprobado", "ausente")



admin.site.register(Persona, PersonaAdmin)
admin.site.register(Turno, TurnoAdmin)
admin.site.register(Clave, ClaveAdmin)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Cuestionario, CuestionarioAdmin)
admin.site.register(Examen, ExamenAdmin)
admin.site.register(Estadistica, EstadisticaAdmin)