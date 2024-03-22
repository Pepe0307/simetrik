![Static Badge](https://img.shields.io/badge/python-3.12-%23ffde57?logo=python)

# Prueba tecnica Simetrik devops 

## Descripcion

Se desarrolló una API en python usando la libreria Flask para retornar nombres de juegos especificados en la URL por el usuario. Tambien se puede hacer la busqueda con juego y consola.
La API está desplegada en AWS en una subnet publica y se conecta a otra instancia en una subnet privada usando el protocolo de comunicación GRPC, en donde se exploraron los metodos de comunicacion "unary", "server side streaming" y "server and client streaming".
La instancia que está en la subnet pública hace el procesamiento del request por parte del usuario y hace el llamado a funciones en la instancia privada para procesar los datos requeridos por el usuario.

## Diagrama de arquitectura y red

La infraestructura se despliega en AWS por medio de Terraform en donde se hicieron modulos para cada uno de los elementos. Una VPC, una subnet publica y una privada, un internet gateway para acceso a internet y un router para hacer que solo la red publica sea accesible desde intternet. Ademas de esto, se configuro una IP, route tables y un NAT para la conectividad de todos los componentes.
![alt text](https://miro.medium.com/v2/resize:fit:640/format:webp/1*1w9mi3WVMaSTCIQG5m9yeA.png)

## Utilizar la API

Para utilizar la API primero se deben desplegar los modulos de Terraform en la carpeta IaC y luego construir los Dockerfile para hacer el despliegue en EC2 o en Kubernetes. Dependiendo de lo que se requiera.
Es importante tener en cuenta que de cualquier manera que se despliegue, se tiene que construir las imagenes de Docker y exponer los puertos 50051 internamente y 5000 para internet para que funcione de la manera esperada.

Después de esto se contacta a la IP especificada en el puerto 5000 y se hace un request de la siguiente manera:
**https://IP:5000/get-game?name=pokemon&console=nintendo**

Donde se tienen varios endpoitns que hacen diferentes funciones: 

**/get-game** en donde se obtiene el nombre del juego especificado con los parametros:
- **?name=nombre_del_juego**

**/get-console** en donde se obtiene el nombre del juego y consola especificado con los parametros: 
- **?name=nombre_del_juego&console=nombre_de_consola**

## Detalles
El codigo python del cliente se encuentra en la carpeta client, el del servidor en la carpeta server. El modelo GRPC que se utilizó está dentro de estas carpeta en una sub carpeta llamada protos. Tambien se pueden encontrar los dockerfiles en donde se hacen las imagenes de los contenedores python desarrollados.

Toda la IaC de Terraform está en la carpeta Iac.