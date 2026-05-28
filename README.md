PROYECTO DISQUERA

Implementa Base de Datos Relacionales

Integrantes:
Martinez Jimenez Kevin Andres
Gonzalez Hernandez Luis Antonio
Barajas Bañuelos Jesus Axel
Mexta Torres Genesis
Gutierrez Ruiz Jesus Javier
Garcia Hernandez Joshua Alexander
Profesor :Jose Christian Romero Sanchez

Grupo: 4AVPG

Fecha de entrega

28 de mayo del 2026



Introducción 
1. Descripción General del Proyecto
“Disquera” es una aplicación web desarrollada con Django utilizando Python y el patrón de arquitectura MVT (Modelo-Vista-Template). El objetivo principal del proyecto es simular el funcionamiento de una tienda discográfica digital, donde los usuarios pueden explorar álbumes musicales, filtrarlos por categorías y realizar compras desde una plataforma web moderna e interactiva.
La aplicación fue diseñada para ofrecer una experiencia sencilla y cómoda para el usuario, permitiendo navegar entre diferentes géneros musicales, consultar información detallada de los álbumes y administrar compras mediante un sistema de carrito y pedidos. Además, el proyecto integra funciones de autenticación para el registro e inicio de sesión de usuarios.
En la parte visual se utilizó Bootstrap 5 para construir una interfaz responsiva y adaptable a distintos dispositivos, logrando una apariencia más moderna y organizada. Mientras tanto, Django se encargó de toda la lógica del sistema, la conexión con la base de datos y el manejo dinámico de la información.

2. Arquitectura de Datos y Evolución del Backend (Modelos)
El funcionamiento interno de la aplicación se basa en una base de datos relacional administrada mediante el sistema de migraciones de Django, lo cual permite agregar nuevas funcionalidades y mantener organizada la estructura del proyecto.
Los modelos principales del sistema son los siguientes:
Gestión de Catálogo (Category y Post)
El modelo Category se utiliza para clasificar los diferentes géneros musicales, como Rock, Reggaetón o Phonk. Cada categoría cuenta con un slug, el cual ayuda a generar URLs más limpias y fáciles de identificar.
Por otro lado, el modelo Post representa los álbumes musicales disponibles dentro de la plataforma. Este almacena información importante como:
•	título,
•	descripción
•	portada
•	precio
•	stock
•	fecha de creación
Gracias a esta estructura es posible mostrar los álbumes dinámicamente dentro de la aplicación.

Sistema Comercial e Inventario
Conforme avanzó el desarrollo del proyecto, se agregaron funciones relacionadas con ventas e inventario.
Para los precios se utilizó DecimalField, ya que permite manejar cantidades monetarias con mayor precisión. También se implementó PositiveIntegerField para el control del stock, evitando cantidades negativas y ayudando a mantener un mejor control de los productos disponibles.

Gestión de Usuarios y Artistas
La aplicación también cuenta con un sistema de autenticación basado en el modelo de usuarios de Django.
Además, mediante relaciones OneToOneField, es posible crear perfiles personalizados asociados a cada usuario. Esto permite almacenar información adicional y mantener separada la lógica de autenticación de otros datos del sistema.

Sistema de Compras (CartItem y Order)
El proyecto incluye un sistema completo de carrito de compras y pedidos.
El modelo CartItem almacena temporalmente los productos que el usuario desea comprar, junto con la cantidad seleccionada. Después, durante el proceso de checkout, se genera una orden mediante el modelo Order, donde se guarda:
•	información del cliente,
•	dirección de envío,
•	total de compra,
•	estado del pedido.
De esta manera la aplicación puede llevar un historial de compras realizadas por cada usuario.

3. Diseño de la Interfaz y Experiencia de Usuario (Frontend)
La interfaz de la aplicación fue desarrollada utilizando Bootstrap 5 y el sistema de templates de Django.
Uno de los conceptos más importantes utilizados fue la herencia de plantillas, la cual permite reutilizar código y mantener un diseño uniforme en todas las páginas.

Plantilla Base (base.html)
El archivo base.html funciona como la estructura principal del proyecto.
Aquí se encuentran elementos globales como:
•	la navbar,
•	Bootstrap,
•	estructura HTML general,
•	estilos compartidos.
Los demás templates heredan esta estructura usando:
{% extends 'disquera/base.html' %}
Esto facilita mucho el mantenimiento del proyecto y evita repetir código innecesariamente.

Página Principal (home.html)
La vista principal funciona como la vitrina de la tienda.
Aquí se muestran:
•	los álbumes disponibles,
•	categorías musicales,
•	botones de navegación,
•	acceso rápido al carrito.
Los productos se presentan mediante cards de Bootstrap para lograr una interfaz más limpia y visualmente agradable.

Vistas de Detalle y Categorías
Las páginas detail.html y category_detail.html permiten que el usuario consulte información más específica.
En estas vistas se muestran:
•	imágenes de los álbumes,
•	descripción,
•	canciones,
•	precio,
•	stock disponible,
•	botones de compra.
Bootstrap ayuda a organizar el contenido mediante filas y columnas responsivas para que la información se vea ordenada tanto en computadora como en dispositivos móviles.

Checkout y Proceso de Compra
La página checkout.html se enfoca en finalizar la compra de manera sencilla.
Aquí el usuario puede ingresar:
•	nombre,
•	dirección,
•	ciudad,
•	código postal.
También se muestra un resumen del pedido con el total a pagar.
Una vez confirmada la compra, la aplicación registra la orden y redirecciona a una página de compra exitosa.

Relaciones:
Order (1) → (N) OrderItem
Post (1) → (N) OrderItem
La función subtotal() calcula el costo individual de cada producto dentro de la orden.


1. Explicación Detallada de settings.py (La Configuración del Sistema)
Carpeta DisqueraProyecto
Este archivo es el encargado de controlar gran parte del comportamiento de Django dentro del proyecto. Aquí se configuran cosas importantes como la seguridad, las aplicaciones instaladas, la base de datos y el manejo de archivos multimedia.
A. Rutas del Sistema y Seguridad	
•	BASE_DIR:
Utiliza la librería pathlib para detectar automáticamente la carpeta donde se encuentra el proyecto. Esto ayuda a que el código funcione en distintos sistemas operativos sin tener que escribir rutas manualmente.
•	SECRET_KEY:
Es una clave única utilizada por Django para temas de seguridad y protección interna del sistema.
•	DEBUG = True:
Esta opción se encuentra activada durante el desarrollo del proyecto. Gracias a esto Django muestra información detallada de los errores cuando algo falla en el código. Aunque es muy útil mientras se programa, cuando la aplicación se sube a internet debe cambiarse a False por seguridad.
•	ALLOWED_HOSTS = []:
Al estar vacío y usar DEBUG = True la aplicación funciona correctamente en el entorno local si el proyecto se publicara en internet aquí se tendría que colocar el dominio del sitio web.
B. Módulos y Extensiones
•	INSTALLED_APPS:
Aquí se registran todas las aplicaciones y herramientas que Django utilizará. En este caso se incluyen aplicaciones nativas como:
o	administración,
o	autenticación de usuarios,
o	sesiones.
También se agregó la aplicación disquera, permitiendo que Django reconozca sus modelos, vistas y rutas.
•	MIDDLEWARE:
Son componentes internos que procesan información antes y después de cada petición del usuario. Por ejemplo:
o	CsrfViewMiddleware protege formularios contra ataques externos.
o	AuthenticationMiddleware permite reconocer usuarios autenticados dentro de las vistas.

C. Base de Datos y Multimedia
•	DATABASES:
El proyecto utiliza sqlite3, que es la base de datos predeterminada de Django. Esta se guarda en un archivo llamado db.sqlite3 y resulta muy práctica para proyectos escolares o en desarrollo porque es ligera y fácil de configurar.
•	MEDIA_URL y MEDIA_ROOT:
Estas configuraciones permiten guardar y mostrar archivos multimedia como las imágenes de los álbumes musicales. Gracias a esto las portadas pueden visualizarse correctamente dentro de la aplicación.


2. Explicación Detallada de urls.py (El Enrutador Global)
El archivo urls.py principal funciona como la puerta de entrada de toda la aplicación. Su función es recibir las solicitudes del navegador y dirigirlas hacia las vistas correspondientes.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('disquera.urls')),
]
Función de cada ruta
•	path('admin/', admin.site.urls):
Conecta el panel de administración de Django. Desde esta sección el administrador puede gestionar categorías, álbumes, usuarios y demás registros del sistema sin necesidad de crear interfaces adicionales.
•	path('', include('disquera.urls')):
Este fragmento le indica a Django que todas las rutas principales de la tienda estarán organizadas dentro del archivo urls.py de la aplicación disquera. Esto ayuda a mantener el proyecto más ordenado y modular.

Bloque Condicional para Archivos Multimedia
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
Este bloque sirve para que Django pueda mostrar imágenes y archivos multimedia mientras el proyecto se encuentra en modo desarrollo. Gracias a esto las portadas de los álbumes se visualizan correctamente en la interfaz.

3. Explicación Detallada de views.py de la Raíz
El archivo views.py contiene la lógica principal de varias funciones de la aplicación. Las vistas se encargan de procesar solicitudes, obtener datos de la base de datos y enviarlos a los templates.

View home(request)
Esta vista controla la página principal del sistema.
Su función principal es:
•	consultar los álbumes activos desde la base de datos,
•	enviarlos al template home.html,
•	mostrar el catálogo musical al usuario.
La vista obtiene la información usando el modelo Post y posteriormente la manda al template mediante variables de contexto.



View detail(request, id)
Esta vista muestra la información detallada de un álbum específico y además controla el sistema de comentarios.
El funcionamiento cambia dependiendo del método utilizado:
•	Si el usuario solamente entra a visualizar el álbum, Django utiliza el método GET y simplemente muestra la página junto con un formulario vacío.
•	Si el usuario envía un comentario, el método cambia a POST. Entonces la vista procesa la información recibida mediante CommentForm(request.POST) y valida que los datos sean correctos usando form.is_valid().
Después el comentario se relaciona con el álbum correspondiente y finalmente se guarda en la base de datos.
Esto permite que los usuarios puedan interactuar con las publicaciones de manera dinámica.

Diseño de la Base de Datos y Relaciones
La base de datos del proyecto “Disquera” fue desarrollada utilizando el ORM de Django, permitiendo manejar la información mediante modelos relacionados entre sí.
La estructura relacional facilita la organización de usuarios, álbumes, artistas, pedidos y comentarios dentro de la plataforma.

Modelo Category
El modelo Category representa las categorías o géneros musicales disponibles dentro del sistema.
Ejemplos:
•	Rock,
•	Pop,
•	Reggaetón,
•	Electrónica.
Campos principales
•	title
•	slug
•	color_hex
Relación
Una categoría puede contener varios álbumes:
Category (1) → (N) Post



Modelo Artist
El modelo Artist almacena información de los artistas registrados.
Campos principales
•	user
•	stage_name
•	bio
Relación
Cada artista se relaciona con un único usuario mediante OneToOneField.
User (1) → (1) Artist

Modelo Post
El modelo Post representa los álbumes musicales dentro de la tienda.
Campos principales
•	title
•	intro
•	body
•	songs
•	price
•	stock
•	image
•	status
Relaciones
•	Un álbum pertenece a una categoría.
•	Un álbum puede pertenecer a un artista.
•	Un álbum puede tener comentarios y especificaciones.
Category (1) → (N) Post
Artist (1) → (N) Post

Modelo Specification
Este modelo permite agregar características adicionales a los álbumes sin modificar directamente la estructura principal del modelo Post.
Ejemplos:
•	año de lanzamiento,
•	sello discográfico,
•	formato musical.

Relación
Post (1) → (N) Specification

Modelo Comment
Permite almacenar comentarios realizados por los usuarios sobre un álbum.
Campos
•	name
•	email
•	body
•	created_at
Relación
Post (1) → (N) Comment

Modelo CartItem
Representa el carrito de compras del usuario.
Cada registro guarda:
•	usuario propietario,
•	producto agregado,
•	cantidad seleccionada.
Relaciones
User (1) → (N) CartItem
Post (1) → (N) CartItem
Además incorpora el método subtotal(), encargado de calcular automáticamente el costo total del producto según su cantidad.

Modelo Profile
El modelo Profile extiende la información básica del usuario.
Campos
•	phone
•	address
•	city
•	postal_code


Relación
User (1) → (1) Profile

Modelo Order
Representa una orden de compra generada por un usuario.
Campos
•	full_name
•	address
•	city
•	postal_code
•	total
•	status
Estados posibles
•	pending,
•	paid,
•	shipped.
Relación
User (1) → (N) Order

Modelo OrderItem
Este modelo almacena los productos individuales comprados dentro de una orden.
Campos
•	quantity
•	price
Gracias a este modelo es posible guardar el detalle completo de cada compra realizada por el usuario.
Diagrama Relacional 
User
 ├── Profile
 ├── Artist
 ├── CartItem
 └── Order

Category
 └── Post
        ├── Specification
        ├── Comment
        ├── CartItem
        └── OrderItem

Order
 └── OrderItem



1. Explicación Detallada de los Modelos (models.py)
Carpeta disquera
Los modelos definen la base de datos de una tienda de música digital o física con manejo de usuarios, artistas, carrito de compras y pasarela de pedidos. Se pueden agrupar en 4 bloques lógicos:
A. Catálogo Musical y Contenido
•	Category: Clasifica la música (ej. "Rock", "Electrónica"). Incluye un slug (una versión de texto amigable para URLs limpias) y un color_hex para personalizar la interfaz visual.
•	Post: Representa el producto o álbum en venta.
o	Tiene relaciones con Artist y Category.
o	Maneja control de inventario (price, stock), estado de publicación (ACTIVE/DRAFT), una lista de canciones en texto (songs) y soporte para carátulas mediante ImageField.
•	Specification: Permite añadir detalles extra y dinámicos a un Post sin alterar la tabla principal (ej. "Sello discográfico: Sony Music", "Año: 2026").
B. Comunidad y Feedback
•	Artist: Extiende el modelo de usuario de Django (User) mediante una relación OneToOneField. Esto significa que un usuario registrado puede ser un artista dentro de la disquera, con su nombre artístico (stage_name) y biografía.
•	Comment: Sistema clásico de retroalimentación donde cualquier visitante puede dejar un comentario en un Post guardando su nombre, email y mensaje.
C. Sistema de Carrito y Perfiles
•	Profile: Al igual que el artista, extiende al User para guardar datos adicionales del comprador necesarios para el envío físico (teléfono, dirección, ciudad, código postal).
•	CartItem: El carrito de compras. Vincula a un usuario con un producto (Post) y una cantidad. Incluye el método inteligente subtotal() que calcula en tiempo real el costo multiplicando el precio por la cantidad ($precio \times cantidad$).
D. Sistema de Órdenes (Historial de Compras)
•	Order: Representa la factura o pedido final. Guarda una "foto fija" de los datos de envío y el total pagado. Maneja estados como pending, paid (pagado) y shipped (enviado).
•	OrderItem: Guarda el desglose de la orden. Es crucial porque almacena el precio del producto en el momento exacto de la compra, evitando que si el precio del álbum sube o baja en el futuro, se altere el historial financiero del usuario.
2. Explicación Detallada de las Vistas (views.py)
Tus vistas controlan el comportamiento del negocio. Utilizan FBV (Vistas basadas en funciones) y decoradores de seguridad.
•	home(request): El punto de entrada. Filtra únicamente los álbumes que estén en estado ACTIVE y los ordena del más reciente al más antiguo (-created_at). Además, envía las categorías para armar el menú de navegación.
•	category_detail(request, slug): Filtra y muestra solo los álbumes que pertenecen a la categoría seleccionada a través del slug. Si la categoría no existe, detiene la ejecución de forma segura con un error 404.
•	detail(request, id): Muestra la página individual de un álbum. Carga el formulario de comentarios (CommentForm) y extrae todos los comentarios asociados a ese post de manera ordenada.
•	cart(request) y add_to_cart(request, id):
1.	Ambas protegidas con @login_required (solo usuarios autenticados).
2.	add_to_cart utiliza get_or_create. Si el producto no estaba en el carrito, lo añade; si ya estaba, simplemente incrementa su cantidad en +1.
•	register(request): Gestiona el registro de nuevos usuarios. Si la petición es POST, procesa el formulario, guarda el usuario, le crea automáticamente su perfil vacío (Profile.objects.create) e inicia su sesión inmediatamente con login(request, user).
•	checkout(request): La vista más compleja y crítica.
1.	Calcula el total del carrito.
2.	Al recibir el formulario válido por POST, crea la orden en la base de datos pero frena su guardado definitivo (commit=False) para inyectarle el usuario, el total y forzar el estado a PAID.
3.	Traspasa cada producto del carrito (CartItem) hacia el historial definitivo (OrderItem).
4.	Vacía el carrito del usuario (items.delete()) y redirige al éxito.
•	success(request) y my_orders(request): La primera muestra la pantalla de agradecimiento post-compra y la segunda lista cronológicamente el historial de pedidos del cliente autenticado.
3. Explicación Detallada de las URLs (urls.py)
Este archivo mapea las peticiones del navegador hacia las vistas que acabamos de explicar, construyendo URLs limpias y dinámicas:
•	Rutas Dinámicas por Texto (slug): category/<slug:slug>/ permite navegar por rutas elegantes como /category/rock/ o /category/pop/.
•	Ruta Raíz: path('', home, name='home') define que la página principal del sitio web ejecutará la vista home.
•	Rutas Dinámicas por ID (int): detail/<int:id>/ y add-to-cart/<int:id>/ capturan el identificador numérico único del registro en la base de datos para pasárselo a la vista (ej. /detail/5/).
•	Vistas Nativas de Django: Para el login/ y logout/, en lugar de escribir código propio en las vistas, estás utilizando de forma muy acertada las vistas preconstruidas de Django (auth_views.LoginView y LogoutView), pasándole la ruta de tu plantilla personalizada.
Gestión de Datos desde Admin
Gestión de Datos Mediante el Panel de Administración
El proyecto utiliza el sistema administrativo integrado de Django para realizar la administración completa de la información del sistema.
El panel administrativo puede accederse mediante la ruta:
/admin/

Este sistema permite realizar operaciones CRUD (Create, Read, Update y Delete) sobre todos los modelos registrados dentro de la aplicación.
Entrada de Datos (Create)
El administrador puede agregar nuevos registros desde el panel de administración utilizando la opción “Add”.
Ejemplos:
•	Crear nuevas categorías musicales.
•	Registrar artistas.
•	Agregar nuevos álbumes.
•	Crear órdenes de compra.
•	Registrar especificaciones de productos.
Cuando el formulario es enviado mediante el botón “Save”, Django almacena automáticamente la información en la base de datos SQLite.

Visualización de Datos (Read)
El panel permite visualizar todos los registros almacenados de manera organizada mediante tablas dinámicas.
Ejemplos:
•	Lista de álbumes.
•	Lista de artistas.
•	Historial de órdenes.
•	Comentarios realizados por usuarios.
•	Inventario disponible.

Actualización de Datos (Update)
Los registros existentes pueden modificarse seleccionando cualquier elemento dentro del administrador.
Ejemplos:
•	Modificar el precio de un álbum.
•	Actualizar el stock disponible.
•	Cambiar la biografía de un artista.
•	Actualizar el estado de una orden a “Pagado” o “Enviado”.
Los cambios se aplican automáticamente después de presionar el botón “Save”.

Eliminación de Datos (Delete)
El administrador también puede eliminar registros desde el panel administrativo utilizando la opción “Delete”.
Ejemplos:
•	Eliminar comentarios no deseados.
•	Borrar álbumes descontinuados.
•	Eliminar categorías obsoletas.
•	Remover órdenes incorrectas.
Antes de eliminar la información, Django solicita una confirmación para evitar pérdidas accidentales de datos.




Ventajas del Sistema Admin de Django
El panel administrativo proporciona:
•	Gestión centralizada de la información.
•	Seguridad mediante autenticación.
•	Validación automática de formularios.
•	Interfaces CRUD generadas automáticamente.
•	Facilidad de mantenimiento del sistema.
Finalmente: Explicación de los Views y su interacción con URLs y Templates
En Django, los views son una parte muy importante de la aplicación, ya que son los encargados de conectar las rutas, la información de la base de datos y las páginas que ve el usuario.
 Básicamente, un view recibe una petición desde una URL, procesa la información necesaria y después manda un template HTML para mostrar una interfaz visual.
El funcionamiento general de la aplicación sería así:
Usuario → URL → View → Template → Página mostrada

Relación entre URLs, Views y Templates
URLs
El archivo urls.py sirve para crear las rutas de la aplicación.
 Cada ruta indica qué view se va a ejecutar cuando el usuario entra a cierta dirección.
Ejemplo:
path('', home, name='home')
Cuando alguien entra a:
http://localhost:8000/
Django ejecuta el view home.

Views
Los views contienen la lógica principal del sistema.
Estos se encargan de:
•	obtener información de la base de datos,
•	procesar formularios,
•	validar usuarios,
•	realizar acciones,
•	enviar datos a los templates.
Ejemplo:
def home(request):

   posts = Post.objects.filter(
       status=Post.ACTIVE
   ).order_by('-created_at')

   categories = Category.objects.all()

   return render(request, 'disquera/home.html', {
       'posts': posts,
       'categories': categories
   })
Aquí el view obtiene los álbumes y categorías para después enviarlos al template home.html.

Templates
Los templates son los archivos HTML que muestran la parte visual de la aplicación.
Por ejemplo:
{% for post in posts %}
El template recibe la variable posts enviada por el view y muestra cada álbum en pantalla.

Explicación de cada View

View home
def home(request):
Este view controla la página principal de la aplicación.
Lo que hace es:
•	obtener los álbumes activos,
•	obtener las categorías,
•	enviar la información al template home.html.
La interacción funciona así:
URL → home() → home.html
En la interfaz se muestran:
•	álbumes,
•	categorías,
•	acceso al carrito.

View category_detail
def category_detail(request, slug):
Este view muestra los álbumes de una categoría específica.
El slug se recibe desde la URL:
path('category/<slug:slug>/', category_detail)
Ejemplo:
/category/rock/
El view:
1.	Busca la categoría.
2.	Filtra los álbumes que pertenecen a ella.
3.	Envía los datos al template category_detail.html.

View detail
def detail(request, id):
Este view muestra la información detallada de un álbum.
La URL manda el id del álbum:
path('detail/<int:id>/', detail)
Ejemplo:
/detail/2/
El view:
•	obtiene el álbum,
•	obtiene los comentarios,
•	crea el formulario,
•	manda todo al template detail.html.
En la interfaz se muestra:
•	imagen,
•	descripción,
•	canciones,
•	precio,
•	botón de compra.

View cart
@login_required
def cart(request):
Este view muestra el carrito de compras.
El decorador:
@login_required
sirve para que solamente usuarios registrados puedan entrar al carrito.
El view:
•	obtiene los productos agregados,
•	calcula el total,
•	manda los datos al template cart.html.

View add_to_cart
def add_to_cart(request, id):
Este view permite agregar productos al carrito.
Proceso:
1.	Obtiene el álbum.
2.	Revisa si ya existe en el carrito.
3.	Si existe:
o	aumenta la cantidad.
4.	Si no existe:
o	crea un nuevo registro.
5.	Redirecciona al carrito.
Interacción:
detail.html → add_to_cart → cart.html


View register
def register(request):
Este view se encarga del registro de usuarios.
Funciones principales:
•	procesa el formulario,
•	crea el usuario,
•	crea el perfil,
•	inicia sesión automáticamente,
•	redirecciona al inicio.
Usa el template:
register.html

View checkout
def checkout(request):
Este es uno de los views más importantes porque controla el proceso de compra.
Aquí se conectan varias partes de la aplicación:
•	carrito,
•	formularios,
•	órdenes,
•	productos.
El proceso funciona así:
1.	Obtiene los productos del carrito.
2.	Calcula el total.
3.	Procesa el formulario de envío.
4.	Crea la orden.
5.	Guarda los productos comprados.
6.	Vacía el carrito.
7.	Redirecciona a success.
Flujo:
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
Este view solamente muestra la pantalla de compra exitosa.
Renderiza el template:
success.html

View my_orders
def my_orders(request):
Este view muestra el historial de pedidos del usuario.
Lo que hace es:
•	obtener las órdenes del usuario,
•	ordenarlas por fecha,
•	enviarlas al template my_orders.html.

Importancia del base.html
El archivo base.html funciona como plantilla principal de toda la aplicación.
Los demás templates usan:
{% extends 'disquera/base.html' %}
Gracias a esto todos comparten:
•	la navbar,
•	estilos,
•	Bootstrap,
•	estructura general.
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
•	pedidos,
•	cerrar sesión.
Y si no ha iniciado sesión aparecen:
•	login,
•	registro.

Conclusión
Los views son una parte fundamental en Django porque son los encargados de hacer que toda la aplicación funcione correctamente.
 Estos conectan las URLs con los templates y permiten mostrar información dinámica al usuario.
Gracias a la interacción entre views, URLs y templates, la aplicación puede:
•	mostrar álbumes,
•	filtrar categorías,
•	registrar usuarios,
•	manejar el carrito,
•	procesar compras,
•	guardar pedidos.
Todo esto permite que el sistema funcione de manera organizada y que el usuario pueda interactuar fácilmente con la aplicación desde la interfaz visual

