# examenModulo2

REQUISITOS TECNICOS:

Configuracion del entorno de desarrollo

	- Configuración de una instancia EC2 en AWS con Amazon Linux.
	- Instalación y configuración de herramientas de desarrollo en la instancia EC2, incluyendo Python, Git y despliega un entorno de desarrollo integrado (IDE) como Cloud9
	- Abrir puerto 5000 para que funcione flask
	- Instalar Flask si aún no lo tienes instalado. Puedes hacerlo ejecutando pip install Flask en tu terminal. Si no tienes pip instalado, debes instalarlo en tu servidor con yum o apt segun tu distribucion linux
	- Instalar la libreria PyMySQL si es necesario con el comando python3 -m pip install PyMySQL
	- Crear base de datos mysql en RDS o en el entorno local
	- Modificar el archivo App.py con las credenciales de tu base de datos

CREAR BASE DE DATOS:

CREATE DATABASE IF NOT EXISTS examen;
USE examen;
CREATE TABLE IF NOT EXISTS formulario (
     id INT AUTO_INCREMENT PRIMARY KEY,
     name VARCHAR(255),
     texto1 VARCHAR(255),
     texto2 VARCHAR(255),
     comparacion BOOLEAN
 );


Sección 3) Pruebas y Depuración ->  python3 test.py
