PROYECTO DISQUERA

Implementa Base de Datos Relacionales

Integrantes:
Martinez Jimenez Kevin Andres
Gonzalez Hernandez Luis Antonio
Barajas Bañuelos Jesus Axel
Mexta Torres Genesis
Gutierrez Ruiz Jesus Javier
Garcia Hernandez Joshua Alexander
Profesor :Jose Christian Romero Hernandez

Grupo: 4AVPG

Fecha de entrega

28 de mayo del 2026




         ÍNDICE:
              portada	1
              Introducción	4
      1. Descripción General del Proyecto	4
      2. Arquitectura de Datos y Evolución del Backend (Modelos)	5
Gestión de Catálogo (Category y Post)	5
Sistema Comercial e Inventario	5
Gestión de Usuarios y Artistas	6
Sistema de Compras (CartItem y Order)	6
               3. Diseño de la Interfaz y Experiencia de Usuario (Frontend)	6
Plantilla Base (base.html)	6
Página Principal (home.html)	6
Vistas de Detalle y Categorías	7
Checkout y Proceso de Compra	7
               1. Explicación Detallada de settings.py (La Configuración del Sistema)	8
Carpeta DisqueraProyecto	8
A. Rutas del Sistema y Seguridad	8
B. Módulos y Extensiones	8
● MIDDLEWARE:	8
C. Base de Datos y Multimedia	8
● DATABASES:	8
       2. Explicación Detallada de urls.py (El Enrutador Global)	9
Función de cada ruta	9
                ● path('admin/', admin.site.urls):	9
                 ● path('', include('disquera.urls')):	9
Bloque Condicional para Archivos Multimedia	9
        3. Explicación Detallada de views.py de la Raíz	9
         Diseño de la Base de Datos y Relaciones	10
Modelo Category	10
Campos principales	10
Relación	10
Modelo Artist	11
Campos principales	11
Relación	11
Modelo Post	11
Campos principales	11
Relaciones	11
Modelo Specification	11
Relación	11
Modelo Comment	12
Campos	12
Relación	12
Modelo CartItem	12
Relaciones	12
Modelo Profile	12
Campos	12
Relación	12
Modelo Order	13
Campos	13
Estados posibles	13
Relación	13
Modelo OrderItem	13
Campos	13
Diagrama Relacional	13
       1. Explicación Detallada de los Modelos (models.py)	14
Carpeta disquera	14
A. Catálogo Musical y Contenido	14
B. Comunidad y Feedback	14
C. Sistema de Carrito y Perfiles	14
D. Sistema de Órdenes (Historial de Compras)	14
               2. Explicación Detallada de las Vistas (views.py)	14
              3. Explicación Detallada de las URLs (urls.py)	15
Gestión de Datos Mediante el Panel de Administración	15
Entrada de Datos (Create)	15
Visualización de Datos (Read)	16
Actualización de Datos (Update)	16
Eliminación de Datos (Delete)	16
Ventajas del Sistema Admin de Django	17
                Finalmente: Explicación de los Views y su interacción con URLs y Templates	17
                Relación entre URLs, Views y Templates URLs	17
                Views	17
                 Templates	18
                 Explicación de cada View	18
                  View detail	19
                  View register	21
                  View checkout	21
                  View success	22
                  Navbar y navegación	23
                               conclusión	23





Introducción
Descripción General del Proyecto

“Disquera” es una aplicación web desarrollada con Django utilizando Python y el patrón de arquitectura MVT (Modelo-Vista-Template). El objetivo principal del proyecto es simular el funcionamiento de una tienda discográfica digital, donde los usuarios pueden explorar álbumes musicales, filtrarlos por categorías y realizar compras desde una plataforma web moderna e interactiva.

La aplicación fue diseñada para ofrecer una experiencia sencilla y cómoda para el usuario, permitiendo navegar entre diferentes géneros musicales, consultar información detallada de los álbumes y administrar compras mediante un sistema de carrito y pedidos. Además, el proyecto integra funciones de autenticación para el registro e inicio de sesión de usuarios.

En la parte visual se utilizó Bootstrap 5 para construir una interfaz responsiva y adaptable a distintos dispositivos, logrando una apariencia más moderna y organizada. Mientras tanto, Django se encargó de toda la lógica del sistema, la conexión con la base de datos y el manejo dinámico de la información.



Arquitectura de Datos y Evolución del Backend (Modelos)

El funcionamiento interno de la aplicación se basa en una base de datos relacional administrada mediante el sistema de migraciones de Django, lo cual permite agregar nuevas funcionalidades y mantener organizada la estructura del proyecto.

Los modelos principales del sistema son los siguientes:

Gestión de Catálogo (Category y Post)

El modelo Category se utiliza para clasificar los diferentes géneros musicales, como Rock, Reggaetón o Phonk. Cada categoría cuenta con un slug, el cual ayuda a generar URLs más limpias y fáciles de identificar.

Por otro lado, el modelo Post representa los álbumes musicales disponibles dentro de la plataforma. Este almacena información importante como:

título,
descripción
portada
precio
stock
fecha de creación

Gracias a esta estructura es posible mostrar los álbumes dinámicamente dentro de la aplicación.


Sistema Comercial e Inventario

Conforme avanzó el desarrollo del proyecto, se agregaron funciones relacionadas con ventas e inventario.

Para los precios se utilizó DecimalField, ya que permite manejar cantidades monetarias con mayor precisión. También se implementó PositiveIntegerField para el control del stock, evitando cantidades negativas y ayudando a mantener un mejor control de los productos disponibles.


el archivo admin.py de la aplicación disquera dentro de Django. Este archivo sirve para registrar los modelos en el panel de administración de Django, permitiendo que el administrador pueda agregar, visualizar, modificar y eliminar información desde la interfaz de admin.
Primero se importa el módulo de administración de Django:
from django.contrib import admin
Después se importan los modelos creados en models.py:
from .models import (
    Category,
    Artist,
    Post,
    Specification,
    Comment,
    CartItem
)
Estos modelos representan las tablas principales de la base de datos del proyecto, por ejemplo:
Category almacena las categorías musicales.
Artist almacena los artistas.
Post representa los álbumes.
Comment guarda comentarios.
CartItem controla el carrito de compras.
Finalmente cada modelo se registra usando:
admin.site.register(Category)
El método admin.site.register() le indica a Django que ese modelo debe aparecer dentro del panel de administración.
Gracias a esto el administrador puede realizar operaciones CRUD directamente desde /admin, es decir:
Crear registros.
Visualizar información.
Modificar datos.
Eliminar registros.
Por ejemplo, al registrar el modelo Post, el administrador puede subir nuevos álbumes musicales, cambiar precios o eliminar publicaciones directamente desde el panel de Django sin necesidad de modificar el código manualmente.
Este archivo es muy importante porque conecta los modelos de la base de datos con la interfaz administrativa del sistema.

Gestión de Usuarios y Artistas

La aplicación también cuenta con un sistema de autenticación basado en el modelo de usuarios de Django.

Además, mediante relaciones OneToOneField, es posible crear perfiles personalizados asociados a cada usuario. Esto permite almacenar información adicional y mantener separada la lógica de autenticación de otros datos del sistema.


Sistema de Compras (CartItem y Order)

El proyecto incluye un sistema completo de carrito de compras y pedidos.

El modelo CartItem almacena temporalmente los productos que el usuario desea comprar, junto con la cantidad seleccionada. Después, durante el proceso de checkout, se genera una orden mediante el modelo Order, donde se guarda:

información del cliente,
dirección de envío,
total de compra,
estado del pedido.

De esta manera la aplicación puede llevar un historial de compras realizadas por cada usuario.



Diseño de la Interfaz y Experiencia de Usuario (Frontend)
La interfaz de la aplicación fue desarrollada utilizando Bootstrap 5 y el sistema de templates de Django.

Uno de los conceptos más importantes utilizados fue la herencia de plantillas, la cual permite reutilizar código y mantener un diseño uniforme en todas las páginas.


Plantilla Base (base.html)

El archivo base.html funciona como la estructura principal del proyecto. Aquí se encuentran elementos globales como:
la navbar,
Bootstrap,
estructura HTML general,
estilos compartidos.

Los demás templates heredan esta estructura usando:

{% extends 'disquera/base.html' %}

Esto facilita mucho el mantenimiento del proyecto y evita repetir código innecesariamente.


Página Principal (home.html)

Aquí se muestran:

los álbumes disponibles,
categorías musicales,
botones de navegación,
acceso rápido al carrito.

Los productos se presentan mediante cards de Bootstrap para lograr una interfaz más limpia y visualmente agradable.


Vistas de Detalle y Categorías

Las páginas detail.html y category_detail.html permiten que el usuario consulte información más específica. En estas vistas se muestran:
imágenes de los álbumes,
descripción,
canciones,
precio,
stock disponible,
botones de compra.

Bootstrap ayuda a organizar el contenido mediante filas y columnas responsivas para que la información se vea ordenada tanto en computadora como en dispositivos móviles.


Checkout y Proceso de Compra

La página checkout.html se enfoca en finalizar la compra de manera sencilla. Aquí el usuario puede ingresar:
nombre,
dirección,
ciudad,
código postal.

También se muestra un resumen del pedido con el total a pagar.
Una vez confirmada la compra, la aplicación registra la orden y redirecciona a una página de compra exitosa.


Relaciones:
Order (1) → (N) OrderItem Post (1) → (N) OrderItem
La función subtotal() calcula el costo individual de cada producto dentro de la orden.

Explicación Detallada de settings.py (La Configuración del Sistema)
Carpeta DisqueraProyecto

Este archivo es el encargado de controlar gran parte del comportamiento de Django dentro del proyecto. Aquí se configuran cosas importantes como la seguridad, las aplicaciones instaladas, la base de datos y el manejo de archivos multimedia.

Rutas del Sistema y Seguridad

BASE_DIR:
Utiliza la librería pathlib para detectar automáticamente la carpeta donde se encuentra el proyecto. Esto ayuda a que el código funcione en distintos sistemas operativos sin tener que escribir rutas manualmente.
SECRET_KEY:
Es una clave única utilizada por Django para temas de seguridad y protección interna del sistema.
DEBUG = True:
Esta opción se encuentra activada durante el desarrollo del proyecto. Gracias a esto Django muestra información detallada de los errores cuando algo falla en el código. Aunque es muy útil mientras se programa, cuando la aplicación se sube a internet debe cambiarse a False por seguridad.
ALLOWED_HOSTS = []:
Al estar vacío y usar DEBUG = True la aplicación funciona correctamente en el entorno local si el proyecto se publicara en internet aquí se tendría que colocar el dominio del sitio web.

Módulos y Extensiones

INSTALLED_APPS:
Aquí se registran todas las aplicaciones y herramientas que Django utilizará. En este caso se incluyen aplicaciones nativas como:
administración,
autenticación de usuarios,
sesiones.

También se agregó la aplicación disquera, permitiendo que Django reconozca sus modelos, vistas y rutas.

MIDDLEWARE:
Son componentes internos que procesan información antes y después de cada petición del usuario. Por ejemplo:
CsrfViewMiddleware protege formularios contra ataques externos.
AuthenticationMiddleware permite reconocer usuarios autenticados dentro de las vistas.


Base de Datos y Multimedia

DATABASES:
El proyecto utiliza sqlite3, que es la base de datos predeterminada de Django. Esta se guarda en un archivo llamado db.sqlite3 y resulta muy práctica para proyectos escolares o en desarrollo porque es ligera y fácil de configurar.
MEDIA_URL y MEDIA_ROOT:
Estas configuraciones permiten guardar y mostrar archivos multimedia como las imágenes de los álbumes musicales. Gracias a esto las portadas pueden visualizarse correctamente dentro de la aplicación.

Explicación Detallada de urls.py (El Enrutador Global)

El archivo urls.py principal funciona como la puerta de entrada de toda la aplicación. Su función es recibir las solicitudes del navegador y dirigirlas hacia las vistas correspondientes.

urlpatterns = [
path('admin/', admin.site.urls), path('', include('disquera.urls')),
]
Función de cada ruta

path('admin/', admin.site.urls):
Conecta el panel de administración de Django. Desde esta sección el administrador puede gestionar categorías, álbumes, usuarios y demás registros del sistema sin necesidad de crear interfaces adicionales.
path('', include('disquera.urls')):
Este fragmento le indica a Django que todas las rutas principales de la tienda estarán organizadas dentro del archivo urls.py de la aplicación disquera. Esto ayuda a mantener el proyecto más ordenado y modular.


Bloque Condicional para Archivos Multimedia
if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Este bloque sirve para que Django pueda mostrar imágenes y archivos multimedia mientras el proyecto se encuentra en modo desarrollo. Gracias a esto las portadas de los álbumes se visualizan correctamente en la interfaz.



Explicación Detallada de views.py de la Raíz

El archivo views.py contiene la lógica principal de varias funciones de la aplicación. Las vistas se encargan de procesar solicitudes, obtener datos de la base de datos y enviarlos a los templates.


View home(request)

Esta vista controla la página principal del sistema. Su función principal es:
consultar los álbumes activos desde la base de datos,
enviarlos al template home.html,
mostrar el catálogo musical al usuario.

La vista obtiene la información usando el modelo Post y posteriormente la manda al template mediante variables de contexto.

View detail(request, id)

Esta vista muestra la información detallada de un álbum específico y además controla el sistema de comentarios. El funcionamiento cambia dependiendo del método utilizado:
Si el usuario solamente entra a visualizar el álbum, Django utiliza el método GET y simplemente muestra la página junto con un formulario vacío.
Si el usuario envía un comentario, el método cambia a POST. Entonces la vista procesa la información recibida mediante CommentForm(request.POST) y valida que los datos sean correctos usando form.is_valid().

Después el comentario se relaciona con el álbum correspondiente y finalmente se guarda en la base de datos. Esto permite que los usuarios puedan interactuar con las publicaciones de manera dinámica.


Diseño de la Base de Datos y Relaciones

La base de datos del proyecto “Disquera” fue desarrollada utilizando el ORM de Django, permitiendo manejar la información mediante modelos relacionados entre sí.

La estructura relacional facilita la organización de usuarios, álbumes, artistas, pedidos y comentarios dentro de la plataforma.


Modelo Category

El modelo Category representa las categorías o géneros musicales disponibles dentro del sistema. Ejemplos:
Rock,
Pop,
Reggaetón,
Electrónica.

Campos principales

title
slug
color_hex

Relación

Una categoría puede contener varios álbumes:

Category (1) → (N) Post

Modelo Artist

El modelo Artist almacena información de los artistas registrados.

Campos principales

user
stage_name
bio

Relación

Cada artista se relaciona con un único usuario mediante OneToOneField.

User (1) → (1) Artist

Modelo Post

El modelo Post representa los álbumes musicales dentro de la tienda.El modelo Profile fue creado para extender la información del usuario autenticado de Django. Aunque Django ya incluye un modelo User, este solamente almacena datos básicos como nombre de usuario, correo y contraseña. Por esa razón se implementó un perfil personalizado para guardar información adicional relacionada con cada usuario.
class Profile(models.Model):
Dentro del modelo se utilizan distintos campos para almacenar información específica del usuario:
image: permite guardar una imagen de perfil.
bio: almacena una pequeña biografía o descripción.
phone: guarda el número telefónico.
address: almacena la dirección.
city: guarda la ciudad.
postal_code: almacena el código postal.
La relación más importante es:
user = models.OneToOneField(User, on_delete=models.CASCADE)
Esta línea crea una relación uno a uno entre el modelo Profile y el modelo User de Django, lo que significa que cada usuario tendrá un único perfil asociado.
Además se utiliza:
on_delete=models.CASCADE
Esto indica que si un usuario es eliminado, automáticamente también se eliminará su perfil relacionado, manteniendo la integridad de la base de datos.
Finalmente el método:
def __str__(self):
    return self.user.username
sirve para mostrar el nombre del usuario dentro del panel de administración de Django, facilitando la identificación de cada perfil registrado.


Modelo Category
El modelo Category representa las categorías musicales dentro de la aplicación.
class Category(models.Model):
Este modelo permite clasificar los álbumes según su género musical, por ejemplo:
Rock,
Pop,
Reggaetón,
Electrónica.
Los campos principales son:
title: almacena el nombre de la categoría.
slug: genera URLs amigables y más organizadas.
color_hex: almacena un color hexadecimal utilizado para personalizar visualmente las categorías.
El campo slug es importante porque ayuda a construir rutas más fáciles de leer dentro de la aplicación. Por ejemplo:
/category/rock/
En lugar de utilizar identificadores numéricos más difíciles de interpretar.
El campo:
color_hex = models.CharField(max_length=7, default='#FFB03A')
permite asignar un color personalizado a cada categoría usando códigos hexadecimales, mejorando la apariencia visual de la interfaz.
Por último el método:
def __str__(self):
    return self.title
permite que Django muestre el nombre de la categoría dentro del panel de administración en lugar de mostrar objetos genéricos.



Modelo Artist
El modelo Artist fue creado para almacenar la información relacionada con los artistas musicales dentro de la plataforma.
class Artist(models.Model):
Este modelo permite separar la información de los artistas del resto de usuarios del sistema, manteniendo una mejor organización dentro de la base de datos.
La relación principal del modelo es:
user = models.OneToOneField(User, on_delete=models.CASCADE)
Esta línea crea una relación uno a uno con el modelo User de Django, lo que significa que cada artista tendrá un único usuario asociado para poder iniciar sesión dentro de la plataforma.
El parámetro:
on_delete=models.CASCADE
indica que si el usuario es eliminado también se eliminará automáticamente el artista relacionado, evitando registros huérfanos dentro de la base de datos.
Los campos principales del modelo son:
stage_name: almacena el nombre artístico.
bio: guarda una biografía o descripción del artista.
Finalmente el método:
def __str__(self):
    return self.stage_name
permite mostrar el nombre artístico dentro del panel de administración de Django de una manera más clara y entendible.
Modelo Post
El modelo Post representa los álbumes o productos musicales disponibles dentro de la aplicación.
class Post(models.Model):
Este es uno de los modelos más importantes del proyecto porque almacena la información principal que se muestra en la tienda.
Dentro del modelo se definen distintos estados para las publicaciones:
ACTIVE = 'active'
DRAFT = 'draft'
active: el álbum se encuentra visible para los usuarios.
draft: el álbum permanece oculto mientras se edita o prepara.
Después se crean las opciones disponibles:
CHOICES_STATUS = (
    (ACTIVE, 'Active'),
    (DRAFT, 'Draft'),
)
Esto permite controlar el estado de las publicaciones desde el panel de administración.
El modelo Post se relaciona con Artist mediante:
artist = models.ForeignKey(
    Artist,
    related_name='posts',
    on_delete=models.CASCADE,
    null=True,
    blank=True
)
Esta relación significa que un artista puede tener muchos álbumes publicados, pero cada álbum pertenece únicamente a un artista.
El parámetro related_name='posts' permite acceder fácilmente a todos los álbumes de un artista.
Mientras que:
null=True,
blank=True
permiten que el álbum pueda existir aunque todavía no tenga un artista asignado.
Después el modelo también se relaciona con Category usando ForeignKey, permitiendo clasificar los álbumes según su género musical.
Gracias a esto la aplicación puede filtrar productos por categorías como Rock, Pop o Electrónica dentro de la interfaz principal.
El modelo Post funciona como el núcleo principal de la tienda ya que conecta artistas, categorías, imágenes, precios y publicaciones dentro del sistema.


Dentro del modelo Post se encuentran varios campos encargados de almacenar toda la información relacionada con los álbumes musicales de la tienda.
El campo:
title = models.CharField(max_length=255)
guarda el título del álbum o publicación.
Después se utiliza:
slug = models.SlugField(max_length=255)
Este campo sirve para generar URLs amigables y más fáciles de leer dentro de la aplicación.
Por ejemplo:
/detail/album-rock/
En lugar de usar rutas complicadas o números largos.
Los campos:
intro = models.TextField()
body = models.TextField()
almacenan la descripción corta y la información completa del álbum.
También aparece:
songs = models.TextField(blank=True, null=True)
el cual permite guardar la lista de canciones del álbum.
Los parámetros blank=True y null=True indican que este campo puede quedar vacío si todavía no se agregan canciones.
Para la parte comercial se utilizan:
price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
Este campo almacena el precio del álbum utilizando valores decimales para mantener mayor precisión en operaciones monetarias.
Mientras que:
stock = models.PositiveIntegerField(default=1)
permite controlar la cantidad de productos disponibles en inventario evitando números negativos.
El campo:
created_at = models.DateTimeField(auto_now_add=True)
guarda automáticamente la fecha y hora en que el álbum fue creado dentro del sistema.
También se utiliza:
status = models.CharField(...)
para controlar si una publicación está activa o en borrador.
Finalmente:
image = models.ImageField(upload_to='upload/', blank=True, null=True)
permite subir imágenes de las portadas de los álbumes y almacenarlas dentro de la carpeta configurada para archivos multimedia.
El método:
def __str__(self):
    return self.title
hace que Django muestre el nombre del álbum dentro del panel de administración en lugar de mostrar objetos genéricos.
Modelo Specification
El modelo Specification fue creado para agregar características adicionales a cada álbum sin modificar directamente el modelo principal Post.
class Specification(models.Model):
Este modelo permite almacenar información flexible como:
año de lanzamiento,
formato musical,
duración,
sello discográfico.
La relación principal es:
post = models.ForeignKey(Post, related_name='specs', on_delete=models.CASCADE)
Esto significa que un álbum puede tener varias especificaciones relacionadas.
Por ejemplo:
Post (1) → (N) Specification
Los campos:
label = models.CharField(max_length=50)
value = models.CharField(max_length=255)
permiten guardar tanto el nombre de la especificación como su valor correspondiente.
Finalmente el método:
def __str__(self):
sirve para mostrar las especificaciones de forma más organizada dentro del panel de administración.
Modelo Comment
El modelo Comment permite almacenar comentarios realizados por los usuarios sobre los álbumes musicales.
class Comment(models.Model):
Este modelo ayuda a que los usuarios puedan interactuar con las publicaciones dejando opiniones o reseñas.
La relación principal es:
post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
Esto indica que un álbum puede tener muchos comentarios asociados.
Los campos principales son:
name: nombre de la persona que comenta.
email: correo electrónico.
body: contenido del comentario.
created_at: fecha en la que se realizó el comentario.
El campo:
created_at = models.DateTimeField(auto_now_add=True)
permite guardar automáticamente la fecha y hora del comentario sin necesidad de ingresarla manualmente.
Gracias a este modelo la aplicación puede mostrar comentarios dinámicamente dentro de la vista detallada de cada álbum.


Modelo Order
El modelo Order representa las órdenes de compra generadas por los usuarios dentro de la aplicación.
class Order(models.Model):
Este modelo es importante porque almacena toda la información relacionada con las compras realizadas en la tienda.
Primero se definen distintos estados para las órdenes:
PENDING = 'pending'
PAID = 'paid'
SHIPPED = 'shipped'
Estos estados permiten controlar el progreso de cada pedido:
pending: la orden aún no ha sido pagada.
paid: la compra fue completada correctamente.
shipped: el pedido ya fue enviado.
Después se crean las opciones disponibles:
STATUS_CHOICES = (
Esto ayuda a que Django muestre una lista seleccionable dentro del panel de administración, facilitando el control de estados de las órdenes.
La relación principal del modelo es:
user = models.ForeignKey(User, on_delete=models.CASCADE)
Esto significa que un usuario puede tener muchas órdenes registradas dentro del sistema.
Por ejemplo:
User (1) → (N) Order
El parámetro:
on_delete=models.CASCADE
indica que si un usuario es eliminado, también se eliminarán todas las órdenes relacionadas con él.
Los campos:
full_name
address
city
postal_code
almacenan la información de envío del cliente durante el proceso de compra.
Mientras que:
total = models.DecimalField(max_digits=10, decimal_places=2)
guarda el total final de la compra utilizando números decimales para mantener precisión en cantidades monetarias.
El campo:
status = models.CharField(...)
permite almacenar el estado actual de la orden utilizando las opciones definidas anteriormente.
También se utiliza:
created_at = models.DateTimeField(auto_now_add=True)
para guardar automáticamente la fecha y hora en que la orden fue creada.
Finalmente el método:
def __str__(self):
    return f"Orden #{self.id}"
sirve para mostrar el número de la orden dentro del panel de administración de una manera más clara y organizada.




Campos principales

title
intro
body
songs
price
stock
image
status

Relaciones

Un álbum pertenece a una categoría.
Un álbum puede pertenecer a un artista.
Un álbum puede tener comentarios y especificaciones.

Category (1) → (N) Post Artist (1) → (N) Post

Modelo Specification

Este modelo permite agregar características adicionales a los álbumes sin modificar directamente la estructura principal del modelo Post.

Ejemplos:

año de lanzamiento,
sello discográfico,
formato musical.

Relación
Post (1) → (N) Specification

Modelo Comment

Permite almacenar comentarios realizados por los usuarios sobre un álbum.

Campos

name
email
body
created_at

Relación
Post (1) → (N) Comment

Modelo CartItem

Representa el carrito de compras del usuario. Cada registro guarda:
usuario propietario,
producto agregado,
cantidad seleccionada.

Relaciones
User (1) → (N) CartItem Post (1) → (N) CartItem

Además incorpora el método subtotal(), encargado de calcular automáticamente el costo total del producto según su cantidad.


Modelo Profile

El modelo Profile extiende la información básica del usuario.

Campos

phone
address
city
postal_code

Relación
User (1) → (1) Profile

Modelo Order

Representa una orden de compra generada por un usuario.

Campos

full_name
address
city
postal_code
total
status

Estados posibles

pending,
paid,
shipped.

Relación
User (1) → (N) Order

Modelo OrderItem

Este modelo almacena los productos individuales comprados dentro de una orden.


Campos

quantity
price

Gracias a este modelo es posible guardar el detalle completo de cada compra realizada por el usuario.






Diagrama de flujo
                           
                           INICIO
                              │
                              ▼
                 Usuario entra al sitio web
                              │
                              ▼
                     urls.py recibe URL
                              │
                              ▼
                 Django busca la ruta correcta
                              │
                              ▼
                   Ejecuta el View asociado
                              │
        ┌─────────────────────────────────────┐
        │                                     │
        ▼                                     ▼
  home(request)                        detail(request,id)
        │                                     │
        ▼                                     ▼
 Obtiene álbumes                       Obtiene álbum
 y categorías                          y comentarios
 desde Post y Category                 desde Post y Comment
        │                                     │
        ▼                                     ▼
 Envía datos a                         Envía datos a
 home.html                             detail.html
        │                                     │
        └─────────────────────────────────────┘
                              │
                              ▼
                   Usuario visualiza álbumes
                              │
                              ▼
                 Usuario agrega al carrito
                              │
                              ▼
                   add_to_cart(request)
                              │
                              ▼
            CartItem guarda producto y cantidad
                              │
                              ▼
                     cart(request)
                              │
                              ▼
                 Obtiene productos del carrito
                              │
                              ▼
                   Calcula subtotal y total
                              │
                              ▼
                     Envía datos a cart.html
                              │
                              ▼
                Usuario procede al checkout
                              │
                              ▼
                   checkout(request)
                              │
          ┌────────────────────────────────┐
          │                                │
          ▼                                ▼
   Obtiene productos                 Procesa formulario
   desde CartItem                    de compra
          │                                │
          └────────────────────────────────┘
                              │
                              ▼
                  Crea Order y OrderItem
                              │
                              ▼
                  Guarda orden en BD
                              │
                              ▼
                    Vacía el carrito
                              │
                              ▼
                   Redirecciona a success
                              │
                              ▼
                    success(request)
                              │
                              ▼
             Muestra compra realizada exitosamente
                              │
                              ▼
                             FIN

INFORMACIÓN DE EXPLICACIÓN DE ESTE DIAGRAMA: en este diagrama se enseña un pequeño reflejo de lo que tiene que ser la estructura de este código con una forma más sencilla de lograr explicar y ejecutar.
Este se muestra las relaciones los procesos de compras los repositorios  como se van ejecutando y funcionando en checkout cómo funciona cómo los va relacionando desde que el usuario se registra de como entra a la pagina lo va a ejecutar.
Como entras a los álbumes como lo seleccionas como lo registras en la compra y mientras vas ejecutando cada una este va ejecutando en los archivos models html etc.  






Explicación Detallada de los Modelos (models.py)

Carpeta disquera
Los modelos definen la base de datos de una tienda de música digital o física con manejo de usuarios, artistas, carrito de compras y pasarela de pedidos. Se pueden agrupar en 4 bloques lógicos:
Catálogo Musical y Contenido
Category: Clasifica la música (ej. "Rock", "Electrónica"). Incluye un slug (una versión de texto amigable para URLs limpias) y un color_hex para personalizar la interfaz visual.
Post: Representa el producto o álbum en venta.
Tiene relaciones con Artist y Category.
Maneja control de inventario (price, stock), estado de publicación (ACTIVE/DRAFT), una lista de canciones en texto (songs) y soporte para carátulas mediante ImageField.
Specification: Permite añadir detalles extra y dinámicos a un Post sin alterar la tabla principal (ej. "Sello discográfico: Sony Music", "Año: 2026").
Comunidad y Feedback
Artist: Extiende el modelo de usuario de Django (User) mediante una relación OneToOneField. Esto significa que un usuario registrado puede ser un artista dentro de la disquera, con su nombre artístico (stage_name) y biografía.
Comment: Sistema clásico de retroalimentación donde cualquier visitante puede dejar un comentario en un Post guardando su nombre, email y mensaje.
Sistema de Carrito y Perfiles
Profile: Al igual que el artista, extiende al User para guardar datos adicionales del comprador necesarios para el envío físico (teléfono, dirección, ciudad, código postal).
CartItem: El carrito de compras. Vincula a un usuario con un producto (Post) y una cantidad. Incluye el método inteligente subtotal() que calcula en tiempo real el costo multiplicando el precio por la cantidad ($precio \times cantidad$).
Sistema de Órdenes (Historial de Compras)
Order: Representa la factura o pedido final. Guarda una "foto fija" de los datos de envío y el total pagado. Maneja estados como pending, paid (pagado) y shipped (enviado).
OrderItem: Guarda el desglose de la orden. Es crucial porque almacena el precio del producto en el momento exacto de la compra, evitando que si el precio del álbum sube o baja en el futuro, se altere el historial financiero del usuario.

Explicación Detallada de las Vistas (views.py)
Tus vistas controlan el comportamiento del negocio. Utilizan FBV (Vistas basadas en funciones) y decoradores de seguridad.
home(request): El punto de entrada. Filtra únicamente los álbumes que estén en estado ACTIVE y los ordena del más reciente al más antiguo (-created_at). Además, envía las categorías para armar el menú de navegación.
category_detail(request, slug): Filtra y muestra solo los álbumes que pertenecen a la categoría seleccionada a través del slug. Si la categoría no existe, detiene la ejecución de forma segura con un error 404.

detail(request, id): Muestra la página individual de un álbum. Carga el formulario de comentarios (CommentForm) y extrae todos los comentarios asociados a ese post de manera ordenada.
cart(request) y add_to_cart(request, id):
Ambas protegidas con @login_required (solo usuarios autenticados).
add_to_cart utiliza get_or_create. Si el producto no estaba en el carrito, lo añade; si ya estaba, simplemente incrementa su cantidad en +1.
register(request): Gestiona el registro de nuevos usuarios. Si la petición es POST, procesa el formulario, guarda el usuario, le crea automáticamente su perfil vacío (Profile.objects.create) e inicia su sesión inmediatamente con login(request, user).
checkout(request): La vista más compleja y crítica.
Calcula el total del carrito.
Al recibir el formulario válido por POST, crea la orden en la base de datos pero frena su guardado definitivo (commit=False) para inyectarle el usuario, el total y forzar el estado a PAID.
Traspasa cada producto del carrito (CartItem) hacia el historial definitivo (OrderItem).
Vacía el carrito del usuario (items.delete()) y redirige al éxito.
success(request) y my_orders(request): La primera muestra la pantalla de agradecimiento post-compra y la segunda lista cronológicamente el historial de pedidos del cliente autenticado.

Explicación Detallada de las URLs (urls.py)
Este archivo mapea las peticiones del navegador hacia las vistas que acabamos de explicar, construyendo URLs limpias y dinámicas:
Rutas Dinámicas por Texto (slug): category/<slug:slug>/ permite navegar por rutas elegantes como /category/rock/ o /category/pop/.
Ruta Raíz: path('', home, name='home') define que la página principal del sitio web ejecutará la vista home.
Rutas Dinámicas por ID (int): detail/<int:id>/ y add-to-cart/<int:id>/ capturan el identificador numérico único del registro en la base de datos para pasárselo a la vista (ej. /detail/5/).
Vistas Nativas de Django: Para el login/ y logout/, en lugar de escribir código propio en las vistas, estás utilizando de forma muy acertada las vistas preconstruidas de Django (auth_views.LoginView y LogoutView), pasándole la ruta de tu plantilla personalizada.
Gestión de Datos desde Admin
Gestión de Datos Mediante el Panel de Administración
El proyecto utiliza el sistema administrativo integrado de Django para realizar la administración completa de la información del sistema.
El panel administrativo puede accederse mediante la ruta:
/admin/

Este sistema permite realizar operaciones CRUD (Create, Read, Update y Delete) sobre todos los modelos registrados dentro de la aplicación.
Entrada de Datos (Create)
El administrador puede agregar nuevos registros desde el panel de administración utilizando la opción “Add”.
Ejemplos:
Crear nuevas categorías musicales.
Registrar artistas.

Agregar nuevos álbumes.
Crear órdenes de compra.
Registrar especificaciones de productos.
Cuando el formulario es enviado mediante el botón “Save”, Django almacena automáticamente la información en la base de datos SQLite.

Visualización de Datos (Read)
El panel permite visualizar todos los registros almacenados de manera organizada mediante tablas dinámicas. Ejemplos:
Lista de álbumes.
Lista de artistas.
Historial de órdenes.
Comentarios realizados por usuarios.
Inventario disponible.

Actualización de Datos (Update)
Los registros existentes pueden modificarse seleccionando cualquier elemento dentro del administrador. Ejemplos:
Modificar el precio de un álbum.
Actualizar el stock disponible.
Cambiar la biografía de un artista.
Actualizar el estado de una orden a “Pagado” o “Enviado”.
Los cambios se aplican automáticamente después de presionar el botón “Save”.

Eliminación de Datos (Delete)
El administrador también puede eliminar registros desde el panel administrativo utilizando la opción “Delete”.
Ejemplos:
Eliminar comentarios no deseados.
Borrar álbumes descontinuados.
Eliminar categorías obsoletas.
Remover órdenes incorrectas.
Antes de eliminar la información, Django solicita una confirmación para evitar pérdidas accidentales de datos.

Ventajas del Sistema Admin de Django
El panel administrativo proporciona:
Gestión centralizada de la información.
Seguridad mediante autenticación.
Validación automática de formularios.
Interfaces CRUD generadas automáticamente.
Facilidad de mantenimiento del sistema.

Finalmente: Explicación de los Views y su interacción con URLs y Templates
En Django, los views son una parte muy importante de la aplicación, ya que son los encargados de conectar las rutas, la información de la base de datos y las páginas que ve el usuario.
Básicamente, un view recibe una petición desde una URL, procesa la información necesaria y después manda un template HTML para mostrar una interfaz visual.
El funcionamiento general de la aplicación sería así:
Usuario → URL → View → Template → Página mostrada


Relación entre URLs, Views y Templates URLs
El archivo urls.py sirve para crear las rutas de la aplicación.
Cada ruta indica qué view se va a ejecutar cuando el usuario entra a cierta dirección. Ejemplo:
path('', home, name='home') Cuando alguien entra a: http://localhost:8000/ Django ejecuta el view home.


Views
Los views contienen la lógica principal del sistema. Estos se encargan de:
obtener información de la base de datos,
procesar formularios,
validar usuarios,
realizar acciones,
enviar datos a los templates.

Ejemplo:
def home(request):


posts = Post.objects.filter( status=Post.ACTIVE
).order_by('-created_at')


categories = Category.objects.all()


return render(request, 'disquera/home.html', { 'posts': posts,
'categories': categories
})
Aquí el view obtiene los álbumes y categorías para después enviarlos al template home.html.



Templates
Los templates son los archivos HTML que muestran la parte visual de la aplicación. Por ejemplo:
{% for post in posts %}
El template recibe la variable posts enviada por el view y muestra cada álbum en pantalla.



Explicación de cada View


View home
def home(request):
Este view controla la página principal de la aplicación. Lo que hace es:
obtener los álbumes activos,
obtener las categorías,

enviar la información al template home.html. La interacción funciona así:
URL → home() → home.html
En la interfaz se muestran:
álbumes,
categorías,
acceso al carrito.



View category_detail
def category_detail(request, slug):
Este view muestra los álbumes de una categoría específica. El slug se recibe desde la URL: path('category/<slug:slug>/', category_detail)
Ejemplo:
/category/rock/ El view:
Busca la categoría.
Filtra los álbumes que pertenecen a ella.
Envía los datos al template category_detail.html.



View detail
def detail(request, id):
Este view muestra la información detallada de un álbum. La URL manda el id del álbum:
path('detail/<int:id>/', detail) Ejemplo:
/detail/2/ El view:
obtiene el álbum,
obtiene los comentarios,
crea el formulario,
manda todo al template detail.html.

En la interfaz se muestra:
imagen,
descripción,
canciones,
precio,
botón de compra.



View cart @login_required def cart(request):
Este view muestra el carrito de compras. El decorador:
@login_required
sirve para que solamente usuarios registrados puedan entrar al carrito. El view:
obtiene los productos agregados,
calcula el total,
manda los datos al template cart.html.



View add_to_cart
def add_to_cart(request, id):
Este view permite agregar productos al carrito. Proceso:
Obtiene el álbum.
Revisa si ya existe en el carrito.
Si existe:
aumenta la cantidad.
Si no existe:
crea un nuevo registro.
Redirecciona al carrito. Interacción:
detail.html → add_to_cart → cart.html

View register
def register(request):
Este view se encarga del registro de usuarios. Funciones principales:
procesa el formulario,
crea el usuario,
crea el perfil,
inicia sesión automáticamente,
redirecciona al inicio. Usa el template:
register.html



View checkout
def checkout(request):
Este es uno de los views más importantes porque controla el proceso de compra. Aquí se conectan varias partes de la aplicación:
carrito,
formularios,
órdenes,
productos.
El proceso funciona así:
Obtiene los productos del carrito.
Calcula el total.
Procesa el formulario de envío.
Crea la orden.
Guarda los productos comprados.
Vacía el carrito.
Redirecciona a success. Flujo:
cart.html
↓
checkout()
↓
checkout.html
↓

success()
↓
success.html



View success
def success(request):
Este view solamente muestra la pantalla de compra exitosa. Renderiza el template:
success.html



View my_orders
def my_orders(request):
Este view muestra el historial de pedidos del usuario. Lo que hace es:
obtener las órdenes del usuario,
ordenarlas por fecha,
enviarlas al template my_orders.html.

Importancia del base.html
El archivo base.html funciona como plantilla principal de toda la aplicación. Los demás templates usan:
{% extends 'disquera/base.html' %} Gracias a esto todos comparten:
la navbar,
estilos,
Bootstrap,
estructura general.
Esto ayuda a que toda la aplicación tenga el mismo diseño y sea más organizada.

Navbar y navegación
El archivo navbar.html ayuda a conectar toda la aplicación mediante enlaces como:
{% url 'home' %}
{% url 'cart' %}
{% url 'login' %}
Estos nombres vienen directamente de urls.py.
Además, la navbar cambia dependiendo de si el usuario inició sesión:
{% if user.is_authenticated %}
Si el usuario está autenticado aparecen opciones como:
pedidos,
cerrar sesión.
Y si no ha iniciado sesión aparecen:
login,
registro.
Conclusión:
En el ecosistema de Django, las views (vistas) se consolidan como el motor operativo y el núcleo de la lógica de negocio de la aplicación. Su importancia radica en su capacidad para actuar como el puente conector definitivo dentro de la arquitectura MVT (Model-View-Template); son las encargadas de interceptar las peticiones HTTP redirigidas por las URLs, procesar la información necesaria (interactuando con la base de datos si es requerido) y renderizar el resultado final a través de los templates para entregárselo al usuario de forma dinámica.
Gracias a esta articulación armónica entre views, URLs y templates, la aplicación no solo es estática, sino que se transforma en una plataforma interactiva capaz de resolver flujos de trabajo complejos. En este proyecto en particular, esta sinergia ha permitido implementar con éxito funcionalidades críticas como:
Gestión de catálogo: La visualización dinámica de álbumes y el filtrado inteligente por categorías.
Autenticación y seguridad: El registro, control y manejo de sesiones de usuarios.
Flujo de comercio electrónico: La administración del carrito de compras en tiempo real, el procesamiento seguro de pagos y el almacenamiento estructurado de pedidos en la base de datos.
En conclusión, el correcto diseño e implementación de las vistas garantiza una separación de responsabilidades eficiente. Esto no solo se traduce en un código limpio, modular y escalable para los desarrolladores, sino también en una experiencia de usuario (UX) fluida, intuitiva y robusta desde la interfaz visual.
¿Por qué funciona bien esta expansión?
Aporta terminología técnica: Introduce conceptos clave como "arquitectura MVT", "lógica de negocio", "peticiones HTTP" y "separación de responsabilidades".
Mejor flujo: Transforma la lista de viñetas en un argumento más sólido y enfocado al impacto que tiene en el negocio o la aplicación (E-commerce/Catálogo).
Cierre redondo: Termina explicando el beneficio doble: para el programador (código limpio) y para el cliente (buena experiencia).

