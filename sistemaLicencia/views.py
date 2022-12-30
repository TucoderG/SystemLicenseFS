import datetime
import random

from django.contrib import messages
from django.contrib.auth import authenticate, get_user, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.generic import View
from sistemaLicencia import models


class registro(View):

    # Clase utilizada para el registro del usuario

    def get(self, request):
        # Metodo para mostrar el formulario al usuario
        form=UserCreationForm()
        return render(request,"registro.html", {"form": form})

    def post(self, request):
        # Metodo que recibe el formulario rellenado por el usuario
        form = UserCreationForm(request.POST)

        if form.is_valid():
            # Se verifica que el formulario se haya completado de forma correcta
            usuario = form.save()
            
            # Logueamos al usuario
            login(request, usuario)

            return redirect("inicio")
        else:

            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            
            return render(request,"registro.html", {"form": form})

def cerrarSesion(request):

    logout(request)
    return redirect("inicio")

def logear(request):
    # Metodo para loguear el usuario en el sistema y errores que pueden ocurrir
    if request.method == "POST":
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario =form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")

            usuario = authenticate(username = nombre_usuario, password = contraseña)

            if usuario is not None:
                login(request, usuario)
                return redirect("inicio")
            else:
                messages.error(request, "Usuario no valido.")

        else:
            messages.error(request, "Informacion incorrecta.")


    form = AuthenticationForm()
    return render(request,"login.html", {"form": form})



def inicio(request):
    return render(request, "inicio.html")

def perfil(request): 
    return render(request, "perfil.html")
   
def obtenerLicencia(request):
    return render(request, "obtenerLicencia.html")


def registrarDatos(request):

    mensaje = "Revise que todos los campos estén completos."

    # Obtengo los datos del usuario
    d = request.POST["dniUsuarioI"]
    nom = request.POST["nombreUsuarioI"]
    ape = request.POST["apellidoUsuarioI"]
    e = request.POST["edadUsuarioI"]
    dire = request.POST["direccionUsuarioI"]
    em = request.POST["emailUsuarioI"]
    tel = request.POST["telefonoUsuarioI"]
    variable = request.POST["anteojosI"]
    if variable == 'si' or variable == 'Si':
        ant = True
    else:
        ant = False

    try:
        # Creo una instancia del usuario
        per = models.Persona(dni = d, nombre = nom, apellido = ape, edad = e, direccion = dire, email = em, telefono = tel, anteojos = ant)
        per.save()
        mensaje = "Datos guardados Correctamente."
        # Si la persona necesita anteojos se le asigna un turno para el medico entre las fechas 01/11/2022 y 30/01/2023
        if ant == True:
            maxid = models.Turno.objects.count()
            inicio = datetime.datetime(2022, 12, 1)
            final =  datetime.datetime(2023, 1, 30)
            turno_random = inicio + (final - inicio) * random.random()
            try:
                turno = models.Turno(idPersona_id = d, nombreTurno = "Revisión ocular", fechaTurno = turno_random)
                turno.save()
                return render(request, "obtenerLicencia.html", {"turno": turno, "mensaje": mensaje})

            except Exception:
                return render(request, "obtenerLicencia.html", {"turno":"No se pudo generar el turno para el medico."})

        # En caso de que la persona no use anteojos se le genera una clave para poder rendir su primer examen
        else:
            # Obtengo el maximo id de clave y establezco la fecha para acceder al examen en 1hs desde el momento en el que se genere
            maxid = models.Clave.objects.count()
            fecha_hoy = datetime.datetime.now()
            hora = datetime.timedelta(hours=1)
            try:
                clave = models.Clave(clave = maxid + 1, fechaExamen = fecha_hoy, tiempoLimite = fecha_hoy + hora, idPersona_id = d)  
                clave.save()
                idE = models.Examen.objects.count()
                examen = models.Examen(idExamen = idE + 1, preguntasCorrectas = 0, clave_id = clave.clave, nombreCuest = "Examen Teorico")
                examen.save()
                mensaje = "Se le ha proporcionado una clave para rendir su primer examen, buena suerte!"
                return render(request, "obtenerLicencia.html", {"mensaje": mensaje, "clave": clave})

            except Exception:
                mensaje = 'No se ah podido generar la clave o el examen!'
                return render(request, "obtenerLicencia.html", {"mensaje": mensaje})

    except Exception:
        return render(request, "obtenerLicencia.html", {"mensaje": mensaje})    


def generarClave(request):
    
    persona = models.Persona.objects.get(nombre__icontains = get_user(request))
    fecha_hoy = datetime.datetime.now().date()
    
    if persona.anteojos == True:
        medico = models.Turno.objects.get(idPersona = persona.dni)

        if medico.fechaTurno > fecha_hoy:
            return render(request, 'generarClave.html', {"mensaje": "Todavia no asistió a la consulta medica."})

    clave = models.Clave.objects.filter(idPersona = persona.dni)

    if clave.count() >= 3:
        return render(request, 'generarClave.html', {"mensaje": "Usted ya se inscribió al maximo de examenes posibles."})

    else:
        maxid = models.Clave.objects.last()
        fecha_ahora = datetime.datetime.now()
        hora = datetime.timedelta(hours=1)

        try:
            clave = models.Clave(clave = maxid.clave + 1, fechaExamen = fecha_ahora, tiempoLimite = fecha_ahora + hora, idPersona_id = persona.dni)
            clave.save()
            idE = models.Examen.objects.count()
            examen = models.Examen(idExamen = idE + 1, preguntasCorrectas = 0, clave_id = clave.clave, nombreCuest = "Examen Teorico")
            examen.save()
            mensaje = "Se le ha proporcionado una clave para rendir su examen, buena suerte!"
            return render(request, 'generarClave.html', {"mensaje": mensaje, "clave":clave})
        except Exception:
            return render(request, 'generarClave.html', {'mensaje': 'Error con la clave/Examen.'})


def examen(request):
    return render(request, "examen.html")

def examenr(request):
    clav = request.GET["clave"]
    # Se busca la clave ingresada por el usuario
    try:
        clave = models.Clave.objects.get(clave = clav)
        examen = models.Examen.objects.get(clave_id = clave)
        if examen.rendido == True:
            return render(request, "examen.html", {"mensaje": "El examen ya fue rendido."})
        horas = datetime.timedelta(hours=3)
        now = timezone.now()
        hora_actual = now - horas

        # Se verifica que la clave no haya expirado y se busca el examen correspondiente a dicha clave
        if clave.tiempoLimite > hora_actual:
            try:
                #exam = models.Examen.objects.get(clave_id = clave.clave)
                #cuest = models.Cuestionario.objects.filter(nombre__icontains = exam.nombreCuest)
                preguntas = models.Pregunta.objects.raw("select * from sistemaLicencia_pregunta where idPregunta in (select idPregunta_id from sistemaLicencia_cuestionario where nombre like 'Examen Teorico')")
                return render(request, "examen.html", {"preguntas": preguntas, "clave": clav})
            except Exception:
                mensaje = 'Error en la creacion de examen/cuestionario'
                return render(request, "examen.html", {"mensaje": mensaje})
        else:
            examen.rendido = True
            examen.save()
            estadistica = models.Estadistica.objects.get()
            estadistica.ausente += 1
            estadistica.save()
            persona = models.Persona.objects.get(clave = clave)
            persona.examenRendidos += 1
            persona.save()

            return render(request, "examen.html", {"mensaje": "El tiempo de rendir el examen ya expiró."})
    
    except Exception:
        return render(request, "examen.html", {"mensaje": "La clave no existe."})


def resultadoExamen(request):
    dic = {}
    persona = models.Persona.objects.get(nombre__icontains = get_user(request))
    clave = models.Clave.objects.filter(idPersona = persona).order_by('-clave').first()
    examen = models.Examen.objects.get(clave = clave)
    
    if examen.rendido == False:
        
        preguntas = models.Pregunta.objects.raw("select * from sistemaLicencia_pregunta where idPregunta in (select idPregunta_id from sistemaLicencia_cuestionario where nombre like 'Examen Teorico')")
        dic[0] = 0
        for key, value in request.GET.items():
            dic[key] = value 

        for pregunta in preguntas:
            
            rta = dic.get(f'{pregunta.idPregunta}')

            if rta in pregunta.respuestaCorrecta:
                examen.preguntasCorrectas += 1
        
    
        examen.rendido = True
        persona.examenRendidos += 1
        examen.save()
        r = models.Estadistica.objects.get()
        r.rendido += 1
        if examen.preguntasCorrectas >= 8:
            r.aprobado += 1
        else:
            r.reprobado += 1
   
        r.save()

        return render(request, "resultadoExamen.html", {"puntaje":examen.preguntasCorrectas})

    else:
        return render(request, "resultadoExamen.html", {"mensaje": "El examen ya fué rendido anteriormente.", "punt": examen.preguntasCorrectas})
    
