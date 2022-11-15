from django.test import TestCase
from sistemaLicencia import Factory
from django.contrib.auth.models import User


class UsuarioTestCase(TestCase):

    def setUp(self):
        # **** Establecer entidades ****

        # **** Persona ****
        self.common_user = Factory.PersonaFactory.build_persona(pdni =11222333,
                                                                pnombre='Prueba',
                                                                papellido='Test',
                                                                pedad=20,
                                                                pdireccion='Calle prueba 123',
                                                                pemail='prueba@email.com',
                                                                ptelefono='+54 9 3329 112233'
                                                                )
        self.common_user.save()
        # *********************************************************************************
        
        # **** Persona con Anteojos ****
        self.common_user_anteojos = Factory.PersonaFactory.build_persona(pdni =11222376,
                                                                pnombre='Test',
                                                                papellido='Prueba',
                                                                pedad=22,
                                                                pdireccion='Calle test 123',
                                                                pemail='test@email.com',
                                                                ptelefono='+54 9 3329 112233',
                                                                panteojos=True
                                                                )
        self.common_user_anteojos.save()


        # **** Login de usuario para pruebas ****
        user = User.objects.create(username = self.common_user.nombre)
        user.set_password('123323')
        user.save()
        self.client.force_login(user)
        # *********************************************************************************

        # **** Turno con el medico ****
        self.turno = Factory.TurnoFactory.build_turno(persona=self.common_user_anteojos, nombre="Revisión ocular", fecha= '2022-11-27')
        self.turno.save()
        # *********************************************************************************

        # **** Clave de examen ****
        self.common_user_clave = Factory.ClaveFactory.build_clave(100,
                                                                self.common_user,
                                                                '2022-09-13',
                                                                '2022-09-13 20:40:00')
        self.common_user_clave.save()

        self.common_user_clave_vigente = Factory.ClaveFactory.build_clave(101,
                                                                self.common_user,
                                                                '2022-11-27',
                                                                '2022-11-27 20:40:00')
        self.common_user_clave_vigente.save()
        # *********************************************************************************

        # **** Examen ****
        self.common_user_examen = Factory.ExamenFactory.build_examen(1,
                                                                    'Examen Teorico',
                                                                    self.common_user_clave,
                                                                    0)
        self.common_user_examen.save()
        self.common_user_examen_vigente = Factory.ExamenFactory.build_examen(2,
                                                                    'Examen Teorico',
                                                                    self.common_user_clave_vigente,
                                                                    0)
        self.common_user_examen_vigente.save()
        # *********************************************************************************

        # **** Estadistica general ****
        self.estadistica = Factory.EstadisticaFactory.build_estadistica()
        self.estadistica.save()
        # *********************************************************************************

        # **** Establecer Preguntas para el cuestionario ****
        self.pregunta1 = Factory.PreguntasFactory.build_preguntas(1,
                                                                'Quien tiene paso?',
                                                                'Peatón',
                                                                'Automovil',
                                                                'Bicicleta',
                                                                'Moto',
                                                                'Peaton')
        self.pregunta1.save()
        self.pregunta2 = Factory.PreguntasFactory.build_preguntas(2,
                                                                'Linea Punteada',
                                                                'Separa carriles',
                                                                'Algo',
                                                                'No se puede cruzar',
                                                                'Estacionar',
                                                                'Separa carriles')
        self.pregunta2.save()
        self.pregunta3 = Factory.PreguntasFactory.build_preguntas(3,
                                                                'Vel Maxima Autopista Auto',
                                                                '130km/h',
                                                                '60km/h',
                                                                '160km/h',
                                                                '30km/h',
                                                                '130km/h')
        self.pregunta3.save()
        self.pregunta4 = Factory.PreguntasFactory.build_preguntas(4,
                                                                'Cosas prohibidas para manejar',
                                                                'Tomar alcohol',
                                                                'Conducir',
                                                                'Estacionar',
                                                                'No hacer nada',
                                                                'Tomar alcohol')
        self.pregunta4.save()
        self.pregunta5 = Factory.PreguntasFactory.build_preguntas(5,
                                                                'En una rotonda',
                                                                'Tiene paso la persona',
                                                                'Se choca',
                                                                'No se puede conducir',
                                                                'Estacionar en la misma',
                                                                'Tiene paso la persona')
        self.pregunta5.save()
        self.pregunta6 = Factory.PreguntasFactory.build_preguntas(6,
                                                                'Senda peatonal',
                                                                'Carril de peaton',
                                                                'carril motocicleta',
                                                                'bicileta',
                                                                'Estacionar en la misma',
                                                                'Carril de peaton')
        self.pregunta6.save()
        self.pregunta7 = Factory.PreguntasFactory.build_preguntas(7,
                                                                'Distancia de seguridad',
                                                                '2 segundos',
                                                                'diferente',
                                                                'no se que puede ser',
                                                                'algo',
                                                                '2 segundos')
        self.pregunta7.save()
        self.pregunta8 = Factory.PreguntasFactory.build_preguntas(8,
                                                                'Distancia de seguridad',
                                                                '50 metros',
                                                                'meh',
                                                                'puede ser',
                                                                'menos',
                                                                '50 metros')
        self.pregunta8.save()
        self.pregunta9 = Factory.PreguntasFactory.build_preguntas(9,
                                                                'Distancia de seguridad',
                                                                'motocicleta',
                                                                'diferente',
                                                                'no se que puede ser',
                                                                'algo',
                                                                'motocicleta')
        self.pregunta9.save()
        # *********************************************************************************

        # **** Cuestionario con sus preguntas ****
        self.cuestionario1 = Factory.CuestionarioFactory.build_cuest(1, 'Examen Teorico', self.pregunta1)
        self.cuestionario1.save()
        self.cuestionario2 = Factory.CuestionarioFactory.build_cuest(2, 'Examen Teorico', self.pregunta2)
        self.cuestionario2.save()
        self.cuestionario3 = Factory.CuestionarioFactory.build_cuest(3, 'Examen Teorico', self.pregunta3)
        self.cuestionario3.save()
        self.cuestionario4 = Factory.CuestionarioFactory.build_cuest(4, 'Examen Teorico', self.pregunta4)
        self.cuestionario4.save()
        self.cuestionario5 = Factory.CuestionarioFactory.build_cuest(5, 'Examen Teorico', self.pregunta5)
        self.cuestionario5.save()
        self.cuestionario6 = Factory.CuestionarioFactory.build_cuest(6, 'Examen Teorico', self.pregunta6)
        self.cuestionario6.save()
        self.cuestionario7 = Factory.CuestionarioFactory.build_cuest(7, 'Examen Teorico', self.pregunta7)
        self.cuestionario7.save()
        self.cuestionario8 = Factory.CuestionarioFactory.build_cuest(8, 'Examen Teorico', self.pregunta8)
        self.cuestionario8.save()
        self.cuestionario9 = Factory.CuestionarioFactory.build_cuest(9, 'Examen Teorico', self.pregunta9)
        self.cuestionario9.save()
        # *********************************************************************************
        
    
    def test_common_user_creation(self):
        # **** Validar que existe la Persona con sus atributos ****
        self.assertEqual(self.common_user.dni, 11222333)
        self.assertEqual(self.common_user.anteojos, False)
        

    def test_common_user_anteojos_creation(self):
        # **** Validar que existe la Persona con sus atributos ****
        self.assertEqual(self.common_user_anteojos.dni, 11222376)
        self.assertEqual(self.common_user_anteojos.anteojos, True)
        
    
    def test_common_user_clave(self):
        # **** Validar que la clave existe ****
        self.assertEqual(self.common_user_clave.clave, 100)
        self.assertEqual(self.common_user_clave.idPersona, self.common_user)
        self.assertEqual(self.common_user_clave.tiempoLimite, '2022-09-13 20:40:00')

    def test_common_user_clave_vigente(self):
        # **** Validar que la clave existe ****
        self.assertEqual(self.common_user_clave_vigente.clave, 101)
        self.assertEqual(self.common_user_clave_vigente.idPersona, self.common_user)
        self.assertEqual(self.common_user_clave_vigente.tiempoLimite, '2022-11-27 20:40:00')

    def test_common_user_examen(self):
        # **** Validar que el examen existe ****
        self.assertEqual(self.common_user_examen.idExamen, 1)
        self.assertEqual(self.common_user_examen.clave, self.common_user_clave)
        self.assertEqual(self.common_user_examen.rendido, False)
    
    def test_common_user_examen_vigente(self):
        # **** Validar que el examen existe ****
        self.assertEqual(self.common_user_examen_vigente.idExamen, 2)
        self.assertEqual(self.common_user_examen_vigente.clave, self.common_user_clave_vigente)
        self.assertEqual(self.common_user_examen_vigente.rendido, False)

    def test_turno_user(self):
        # **** Validar que existe el turno para el medico del usuario ****
        self.assertEqual(self.turno.idPersona, self.common_user_anteojos)



    def test_registro_usuario(self):
        # **** Validar funcion de REGISTRO ****
        user = self.client.post('/registro', {'username': 'Gian', 'password': 'Act123323'})
        self.assertEqual(user.status_code, 200)

    def test_ingreso_usuario(self):
        # **** Validar funcion de LOGIN ****
        usuario = self.client.post('/login', {'username': 'Gian', 'password': 'Act123323'})
        self.assertEqual(usuario.status_code, 200)

    def test_views_inicio(self):
        # **** Validar funcion de inicio ****
        request = self.client.post('/inicio')
        self.assertEqual(request.status_code, 200)

    def test_views_perfil(self):
        # **** Validar funcion de perfil ****
        request = self.client.post('/perfil')
        self.assertEqual(request.status_code, 200)
    
    def test_views_examem(self):
        # **** Validar funcion de perfil ****
        request = self.client.post('/examen')
        self.assertEqual(request.status_code, 200)

    def test_views_obtener_licencia(self):
        # **** Validar funcion de obtenerLicencia ****
        obtenerLicencia = self.client.get('/obtenerLicencia?/')
        self.assertEqual(obtenerLicencia.status_code, 200)

    def test_views_registrarDatosSinAnteojos(self):
        # **** Validar funcion de registrar datos del usuario ****
        registrarDatosSinAnteojos = self.client.post('/registrarDatos', {'dniUsuarioI': self.common_user.dni,
                                                'nombreUsuarioI': self.common_user.nombre,
                                                'apellidoUsuarioI': self.common_user.apellido,
                                                'edadUsuarioI': self.common_user.edad,
                                                'direccionUsuarioI': self.common_user.direccion,
                                                'emailUsuarioI': self.common_user.email,
                                                'telefonoUsuarioI': self.common_user.telefono,
                                                'anteojosI': 'no'})
        
        self.assertEqual(registrarDatosSinAnteojos.status_code, 200)
        self.assertContains(registrarDatosSinAnteojos, 'Se le ha proporcionado una clave para rendir su primer examen, buena suerte!')


    def test_views_registrarDatosConAnteojos(self):
        # **** Validar funcion de registrar datos del usuario ****
        registrarDatosConAnteojos = self.client.post('/registrarDatos',{'dniUsuarioI': self.common_user.dni,
                                                'nombreUsuarioI': 'Antonio',
                                                'apellidoUsuarioI': self.common_user.apellido,
                                                'edadUsuarioI': self.common_user.edad,
                                                'direccionUsuarioI': self.common_user.direccion,
                                                'emailUsuarioI': self.common_user.email,
                                                'telefonoUsuarioI': self.common_user.telefono,
                                                'anteojosI': 'si'})

        self.assertEqual(registrarDatosConAnteojos.status_code, 200)
        self.assertContains(registrarDatosConAnteojos, 'Datos guardados Correctamente.')



    # ************* Generar Clave *********************
    def test_views_generar_clave_exito(self):
        # **** Validar funcion para generar clave a un usuario ****
        
        request = self.client.get('/generarClave?')

        self.assertEqual(request.status_code, 200)
        self.assertEqual(request.context.get('mensaje'), 'Se le ha proporcionado una clave para rendir su examen, buena suerte!')

    def test_views_generar_clave_3(self):
        # **** Validar funcion verificando que el usuario ya cuenta con 3 o mas claves para rendir ****
        clave2 = Factory.ClaveFactory.build_clave(2, self.common_user,'2022-09-13' ,'2022-09-13 20:40:00')
        clave2.save()
        clave3 = Factory.ClaveFactory.build_clave(3, self.common_user,'2022-09-14' ,'2022-09-14 20:40:00')
        clave3.save()

        request = self.client.get('/generarClave?')
        self.assertEqual(request.status_code, 200)
        self.assertEqual(request.context.get('mensaje'), 'Usted ya se inscribió al maximo de examenes posibles.')
    

    def test_views_generar_clave_medico(self):
        # **** Validar funcion para verificar si no asistió a la consulta medica
        self.client.logout()
        user = User.objects.create(username= self.common_user_anteojos.nombre)
        user.set_password('12345')
        user.save()
        self.client.force_login(user)
        request = self.client.get('/generarClave?')

        self.assertEqual(request.status_code, 200)
        self.assertEqual(request.context.get('mensaje'), 'Todavia no asistió a la consulta medica.')

    # ************* Examen *********************
    def test_views_examen_vigente(self):
        # **** Validar funcion para brindar las preguntas de un examen vigente
        request = self.client.get('/examenr', {'clave': '101'})
        self.assertEqual(request.status_code, 200)
        self.assertEqual(request.context.get('clave'), '101')

    def test_views_examen_vencido(self):
        # **** Validar funcion para brindar las preguntas de un examen vencido
        request = self.client.get('/examenr', {'clave': '100'})
        self.assertEqual(request.status_code, 200)
        self.assertEqual(request.context.get('mensaje'), 'El tiempo de rendir el examen ya expiró.')
    
    def test_views_resultadoExamen_reprobado(self):
    # **** Validar funcion de calcular el puntaje del examen echo ****
        
        request = self.client.get('/resultadoExamen?', {
                                                    '1': 'Peaton',
                                                    '2': 'Separa carriles',
                                                    '3': '130km/h',
                                                    '4': 'Tomar alcohol',
                                                    '5': 'Tiene paso la persona',
                                                    '6': 'Carril de circulacion',
                                                    '7': '5 segundos',
                                                    '8': '30 metros',
                                                    '9': 'estacionar',
                                                    '10': 'bici'
        })
        
        self.assertEqual(request.status_code, 200)
        self.assertEqual(request.context.get('puntaje'), 5)

    def test_views_resultadoExamen_aprobado(self):
    # **** Validar funcion de calcular el puntaje del examen echo ****
        
        request = self.client.get('/resultadoExamen?', {
                                                    '1': 'Peaton',
                                                    '2': 'Separa carriles',
                                                    '3': '130km/h',
                                                    '4': 'Tomar alcohol',
                                                    '5': 'Tiene paso la persona',
                                                    '6': 'Carril de peaton',
                                                    '7': '2 segundos',
                                                    '8': '50 metros',
                                                    '9': 'motocicleta',
                                                    '10': 'bici'
        })
        
        self.assertEqual(request.status_code, 200)
        self.assertEqual(request.context.get('puntaje'), 9)
