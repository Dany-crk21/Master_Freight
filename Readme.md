# 📦 Proyecto de Fletes y Mudanzas

## 📌 Definición del proyecto
Aplicación web destinada a contratar servicios de fletes y mudanzas a nivel provincial.  
El objetivo es facilitar a los usuarios el transporte de electrodomésticos, muebles u objetos voluminosos mediante una plataforma confiable e intuitiva.  

---

## 📝 Descripción breve de la problemática regional
En la región existe una demanda creciente de servicios de transporte de cargas pequeñas y medianas, sin embargo, los usuarios suelen enfrentar problemas como:  
- Dificultad para encontrar fleteros disponibles.  
- Falta de información clara sobre precios y tiempos.  
- Escasa seguridad y trazabilidad del servicio.  

La aplicación busca resolver estas problemáticas mediante **digitalización y transparencia**.

---

## 🗂️ Identificación de entidades principales
1. **Usuario** (cliente que solicita el servicio).  
2. **Fletero** (transportista con vehículo registrado).  
3. **Servicio de Flete/Mudanza** (reserva con origen, destino, fecha, carga y precio).  

---

## 🔗 Modelo de relaciones
Diagrama simple de entidades y relaciones:  


---

## 👥 Integrantes
- Andrada Daniel  
- Vargas Matías  
- Juan Brian  
- Duffau Gianfranco
- Miranda Alejo

---

## ⚙️ Configuración del entorno

### 1. Crear un entorno virtual
**Linux / macOS:**
```bash
python3 -m venv <nombre_del_entorno>
```
**Windows:**
```bash
python -m venv <nombre_del_entorno>
```
### 2. Activar el entorno virtual
**Linux / macOS:**
```bash
source <nombre_del_entorno>/bin/activate
```
**Windows:**
```bash
<nombre_del_entorno>\Scripts\activate
```

### 3. Instalar dependencias:
```bash
pip install Flask Flask-SQLAlchemy PyMySQL python-dotenv
```

## 🛢️ Configuración de la base de datos
### Antes de ejecutar la aplicación, configurar las variables de entorno:

```env
MYSQL_USER=<tu_usuario>
MYSQL_PASSWORD=<tu_contraseña>
MYSQL_HOST=<host_de_mysql>
MYSQL_DATABASE=<nombre_de_la_base_de_datos>
```

## 🚀 Instalación y ejecución

### 1. Clona el repositorio: 
git clone <url_del_repositorio>

### 2. Accede al directorio del proyecto:
```bash
cd <nombre_del_proyecto>
```
### 3. Instala las dependencias desde el requirements.txt
```bash
pip install -r requirements.txt
```
### 4. Ejecuta la aplicacion:
```bash
python app.py
```