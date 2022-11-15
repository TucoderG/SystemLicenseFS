from sistemaLicencia.models import Persona, Clave, Turno, Examen, Cuestionario, Pregunta, Estadistica



class PersonaFactory:
    def build_persona(pdni, pnombre, papellido, pedad, pdireccion, pemail, ptelefono, panteojos = False, pexamrendido = 0):
        return Persona(
            dni=pdni,
            nombre= pnombre,
            apellido=papellido,
            edad=pedad,
            direccion=pdireccion,
            email=pemail,
            telefono=ptelefono,
            anteojos=panteojos,
            examenRendidos=pexamrendido
       )

class TurnoFactory:
    def build_turno(persona, nombre, fecha):
        return Turno(
            idPersona = persona,
            nombreTurno = nombre,
            fechaTurno = fecha
        )

class ClaveFactory:
    def build_clave(id, persona, fecha, tiempo):
        return Clave(
            clave = id,
            idPersona = persona,
            fechaExamen = fecha,
            tiempoLimite = tiempo
       )

class ExamenFactory:
    def build_examen(id, nombre, clave, pCorrectas):
        return Examen(
            idExamen = id,
            nombreCuest = nombre,
            clave = clave,
            preguntasCorrectas = pCorrectas
        )

class CuestionarioFactory:
    def build_cuest(id, nomb, idPta):
        return Cuestionario(
            idCuestionario = id,
            nombre = nomb,
            idPregunta = idPta
        )

class EstadisticaFactory:
    def build_estadistica():
        return Estadistica(
            rendido = 0,
            aprobado = 0,
            reprobado = 0,
            ausente = 0
        )

class PreguntasFactory:
    def build_preguntas(id, preg, resp1, resp2, resp3, resp4, respCorrect):
        return Pregunta(
            idPregunta = id,
            pregunta = preg,
            respuesta1 = resp1,
            respuesta2 = resp2,
            respuesta3 = resp3,
            respuesta4 = resp4,
            respuestaCorrecta = respCorrect
        )