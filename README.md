# python_docker
 Docker Scripts

# Recomendaciones
 - Crear directorio "python_docker" y copiar archivos del repositorio.
 
# Actividades 
 - 	Instalación de Python y despliegue las librerías instaladas
	o	Instalar Python 3.9.6
	o	Instalar librerías a través de los siguientes comandos:
			pip3 install Flask
			pip3 install PyYAML==5.3.1
			pip3 install requests==2.25.0
			pip3 freeze > requirements.txt
			
-	Copiar aplicación Python “lista_librerias.py” y dejarla en directorio “python-docker”

-	Crear imagen Docker
	o	Acceder al directorio “python-docker” y ejecutar el siguiente comando:
			docker build --tag python-docker .

-	Configuración entorno docker
	o	En host:
			Configurar permisos de usuario
			Activar auditoria de archivos y directorios
	o	En Docker Daemon:
			Limitar tráfico entre contenedores
	o	En Imágenes:
			Levantar y fixear vulnerabilidades de la imagen
			Ejecución con usuario NOROOT
			Validar integridad de imágenes
			Configurar conexiones a Bases de Datos fuera de archivos “dockerfile”
			•	Privilegiar el uso de Kubernetes o Docker Swarm

-	Versionar la imagen recién creada con Tags y eliminar el tag original (latest)
	o	Ejecutar el siguiente comando:
			docker tag python-docker:latest python-docker:v1.0.0
			docker rmi python-docker:latest

-	Ejecutar contenedor creado
	o	Ejecutar el siguiente comando:
			docker run python-docker:v1.0.0

