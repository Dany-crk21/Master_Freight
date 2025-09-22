Definición del proyecto

Descripción breve de la problemática regional elegida:

Identificación de al menos 3 entidades principales:

Usuario

Modelo de relaciones (diagrama ER o esquema relacional simple).

Nombres de los integrantes:

Andrada Daniel, Vargas Matias, Juan Brian

Instrucciones para instalar dependencias, correr migraciones y levantar el servidor.

Configuracion del entorno

1.Crear un entorno virtual

En Linux / macOS:
python3 -m venv <nombre_del_entorno>

En Windows:
python -m venv <nombre_del_entorno>

2.Activar el entorno virtual

En Linux / macOS:
source <nombre_del_entorno>/bin/activate

En Windows:
<nombre_del_entorno>\Scripts\activate

3.Instalar dependencias:
pip install Flask Flask-SQLAlchemy PyMySQL python-dotenv

Configuración de la base de datos
Antes de ejecutar la aplicación, debes configurar las siguientes variables de entorno:

MYSQL_USER=<tu_usuario>
MYSQL_PASSWORD=<tu_contraseña>
MYSQL_DATABASE=<nombre_de_la_base_de_datos>
MYSQL_HOST=<host_de_mysql>

Instalacion y ejecución

1.Clona el repositorio: 
git clone <url_del_repositorio>

2.Accede al directorio del proyecto:
cd <nombre_del_proyecto>

3.Instala las dependencias desde el archivo requirements.txt:
pip install -r requirements.txt

4.Ejecuta la aplicacion:
python app.py