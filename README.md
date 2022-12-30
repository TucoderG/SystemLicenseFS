# SystemLicenseFS

Aplicacion web sobre un sistema para obtener la licencia de conducir.

Tecnologias utilizadas:
Django (python) - HTML (Codigo CSS dentro del mismo por el momeno) - Sqlite3 - Visual Studio Code.

Levantar un servidor local:
Debemos estar dentro de la carpeta principal e introducir el comando "python manage.py runserver",
luego dirigirse a la direccion local que se nos dará al ejecutar el comando.

Una vez en dicha dirección deberemos agregar "/inicio" para empezar con el uso de la aplicacion web.

Test unitario:
Debemos estar dentro de la carpeta principal e introducir "python manage.py test" para correr el archivo "/sistemaLicencia/tests.py"
y todos los metodos que lleven los nombres "test.py", "*_test.py", "test_*.py" se ejecutaran como pruebas o tests.

Si instalamos la libreria "coverage" podremos utilizar "coverage run manage.py test" para ejecutar los test de la misma manera que el comando anterior,
pero ademas tambien podremos consultar las lineas que no se estan utilizando de los archivos en los que estemos trabajando con "coverage report -m".
