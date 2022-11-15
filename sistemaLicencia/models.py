from django.db import models

# en la terminal escribir "python manage.py shell"
# luego escribir "from nombreApp.models import NombreTabla"

# INSERTAR -  "v_variable=NombreClase.object.create(nombre_parametro='valor')"
# UPDATE   -  "v_variable.NombreColumna= 'algo'"
# DELETE   -  "v_variable_d = nombreClase.object.get(id = 5)" --> trae el objeto con id = 5
#             "v_variable_d.delete()"
# SELECT   -  "v_var = NombreTabla.object.all()" --> guarda en la variable todos los registros de la tabla ingresada, para ver la lista ejecuto la variable

class Persona(models.Model):
    dni = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=60, blank=True, null=True)
    email = models.EmailField(max_length=50, unique=True)
    telefono = models.CharField(max_length=20)
    anteojos = models.BooleanField(default = False)
    examenRendidos = models.IntegerField(default = 0)

    def __str__(self):
        return f'{self.dni}'


class Clave(models.Model):
    clave = models.IntegerField(primary_key = True)
    idPersona = models.ForeignKey(Persona, on_delete = models.CASCADE)
    fechaExamen = models.DateField(null = False)
    tiempoLimite = models.DateTimeField(null = False)
    
    def __str__(self):
        return f'{self.clave}'


class Turno(models.Model):
    idPersona = models.ForeignKey(Persona, on_delete = models.CASCADE)
    nombreTurno = models.CharField(max_length = 40, null = False)
    fechaTurno = models.DateField(null = False)

    def __str__(self):
        return f'{self.nombreTurno}'



class Pregunta(models.Model):
    idPregunta = models.IntegerField(primary_key = True)
    pregunta = models.CharField(max_length = 150)
    respuesta1 = models.CharField(max_length = 200)
    respuesta2 = models.CharField(max_length = 200)
    respuesta3 = models.CharField(max_length = 200)
    respuesta4 = models.CharField(max_length = 200)
    respuestaCorrecta = models.CharField(max_length = 200)

    def __str__(self):
        return f'{self.idPregunta}'


class Cuestionario(models.Model):
    idCuestionario = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    idPregunta = models.ForeignKey(Pregunta, on_delete = models.CASCADE)
    

    def __str__(self):
        return f'{self.idCuestionario}'

class Examen(models.Model):
    idExamen = models.IntegerField(primary_key = True)
    nombreCuest = models.CharField(max_length = 50, default = "Examen Teorico")
    clave = models.ForeignKey(Clave, on_delete = models.CASCADE)
    rendido = models.BooleanField(default = False)
    preguntasCorrectas = models.IntegerField()

    def __str__(self):
        return f'{self.idExamen}'


class Estadistica(models.Model):

    rendido = models.IntegerField()
    aprobado = models.IntegerField()
    reprobado = models.IntegerField()
    ausente = models.IntegerField()

    def __str__(self):
        return f'Examenes rendidos: {self.rendido} - Aprobados: {self.aprobado} - Reprobados: {self.reprobado} - Ausentes: {self.ausente}'

