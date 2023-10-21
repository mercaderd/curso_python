# 📗 Lección 17: Peticiones HTTP y consumo de APIs

**[Índice](../README.md)**

**[Anterior](../16_Modulos/README.md)**

## Lo básico de HTTP 

[**HTTP**](https://developer.mozilla.org/es/docs/Web/HTTP), de sus siglas en inglés: *"Hypertext Transfer Protocol"*, es el nombre de un protocolo el cual nos permite realizar una petición de datos y recursos, como pueden ser documentos HTML. Es la base de cualquier intercambio de datos en la Web, y un protocolo de estructura cliente-servidor. Así funcionan los navegadores web.

![Esquema básico de HTTP](https://developer.mozilla.org/es/docs/Web/HTTP/Overview/fetching_a_page.png)

La comunicación entre un cliente(navegador web, App móvil o un programa de python) y un servidor en internet se produce mediante una serie de *peticiones* y *respuestas*. El cliente inicia el proceso haciendo una petición al servidor web y recibe una respuesta del servidor web. Con sucesivas peticiones y respuestas se completa la comunicación.

Las peticiones y respuestas HTTP, comparten una estructura similar, compuesta de:
1. Una línea de inicio ('start-line' en inglés) describiendo la petición a ser implementada, o su estado, sea de éxito o fracaso. Esta línea de comienzo, es siempre una única línea.
2. Un grupo opcional de cabeceras HTTP, indicando la petición o describiendo el cuerpo ('body' en inglés) que se incluye en el mensaje.
3. Una línea vacía ('empty-line' en inglés) indicando toda la meta-información ha sido enviada.
4. Un campo de cuerpo de mensaje opcional ('body' en inglés) que lleva los datos asociados con la petición (como contenido de un formulario HTML), o los archivos o documentos asociados a una respuesta (como una página HTML, o un archivo de audio, vídeo ... ) . La presencia del cuerpo y su tamaño es indicada en la línea de inicio y las cabeceras HTTP.

La línea de inicio y las cabeceras HTTP, del mensaje, son conocidas como la **cabeza de la peticiones** o **headers**, mientras que su contenido en datos se conoce como el **cuerpo del mensaje** o **payload**.

![Estructura mensajes HTTP](https://developer.mozilla.org/es/docs/Web/HTTP/Messages/httpmsgstructure2.png)

### Peticiones HTTP - Requests

#### Línea de inicio

La línea de inicio está formada por tres elementos:

1. Un método HTTP (GET, POST u otros), que describan la acción que se pide sea realizada. Por ejemplo, GET indica que un archivo ha de ser enviado hacia el cliente, o POST indica que hay datos que van a ser enviados hacia el servidor (creando o modificando un recurso, o generando un documento temporal para ser enviado).
2. El destino de la petición, normalmente es una URL, o la dirección completa del protocolo, puerto y dominio también suelen ser especificados por el contexto de la petición. El formato del objetivo de la petición varia según los distintos métodos HTTP.
3. La versión de HTTP, la cual define la estructura de los mensajes, actuando como indicador, de la versión que espera que se use para la respuesta.

Ejemplo de una línea de inicio: GET http://developer.mozilla.org/es/docs/Web/HTTP/Messages HTTP/1.1

#### Cabeceras - Headers

Las cabeceras (en inglés headers) HTTP permiten al cliente y al servidor enviar información adicional junto a una petición o respuesta. Una cabecera de petición esta compuesta por su nombre (no sensible a las mayusculas) seguido de dos puntos ':', y a continuación su valor (sin saltos de línea).

![Cabeceras de petición HTTP](https://developer.mozilla.org/es/docs/Web/HTTP/Messages/http_request_headers3.png)

En las cabeceras van también las cookies, si las hubiera para el dominio al que se envía la petición.

#### Cuerpo - Payload

La parte final de la petición el el cuerpo, es el contenido de la petición. No todas las peticiones llevan uno: las peticiones que reclaman datos, como GET, normalmente no necesitan ningún cuerpo. Las peticiones que envían datos, como POST, normalmente siempre llevan un cuerpo.
El cuerpo de la petición puede ser datos en formato JSON, puede ser una imágen, cualquier tipo de archivo, ...

### Respuestas HTTP - Responses

#### Linea de estado

La línea de inicio de una respuesta HTTP, se llama la línea de estado, y contienen la siguiente información:

1. La versión del protocolo, normalmente HTTP/1.1.
2. Un código de estado, indicando el éxito o fracaso de la petición. Códigos de estado muy comunes son: 200, 404, o 302
3. Un texto de estado, que es una breve descripción, en texto, a modo informativo, de lo que significa el código de estado, con el fin de que una persona pueda interpretar el mensaje HTTP.

Una línea de estado típica es por ejemplo: HTTP/1.1 404 Not Found.

#### Cabeceras - Headers

Contiene las cabeceras de la respuesta con la misma estructura que las cabezas de la petición. En las cabeceras van también las cookies que el servidor envía al cliente.

#### Cuerpo - Payload

La última parte del mensaje de respuesta el es 'cuerpo'. No todas las respuestas tienen uno, respuestas con un código de estado como 201 o 204 (en-US) normalmente prescinden de él.

### Códigos de respuesta

- 200: OK
- 301: Moved Permanently
- 400: Bad Request
- 401: unauthorized
- 403: Forbidden
- 404: Not Found
- 418: I'm a teapot 😂

## Requests en Python

[Requests](https://requests.readthedocs.io/en/latest/) permite enviar peticiones HTTP/1.1 de forma extremadamente sencilla. No es necesario añadir manualmente cadenas de consulta a las URL ni codificar los datos POST. Keep-alive y HTTP connection pooling son 100% automáticos, gracias a urllib3.

Hacer una petición GET:

```python
import requests

r = requests.get('https://www.aepd.es')
print(r.status_code)
print(r.request.headers)
print(r.headers)
if r.status_code == requests.codes.ok:
    print(r.text)
```

## API REST

API es el acrónimo de interfaz de programación de aplicaciones (application programming interface en inglés). Es un conjunto de reglas bien definidas que se utilizan para especificar formalmente la comunicación entre dos componentes de software. 

Una API REST es una interfaz de comunicación entre sistemas de información que usa el protocolo de transferencia de hipertexto (hypertext transfer protocol o HTTP, por su siglas en inglés) para obtener datos o ejecutar operaciones sobre dichos datos en diversos formatos, como pueden ser XML o JSON. En su mayoría las API REST actuales utilizan JSON.

Para utilizar una API, debe realizar una petición a un servidor web remoto y recuperar los datos de respuesta en JSON.

Vamos a utilizar una API de una tienda online fake para pruebas, porque es una API sencilla y gratuita que no requiere autenticación.

#### Métodos HTTP y códigos de  en API REST

Los métodos HTTP le dicen a la API qué queremos hacer:

| Método   | Acción   |
|----------|----------|
| GET      | Pedir datos                   |
| POST     | Añadir datos                  | 
| PUT      | Actualizar datos existentes   |
| DELETE   | Eliminar datos                |

Una vez que una API REST recibe y procesa una solicitud HTTP, devuelve una respuesta con un código de estado HTTP. Este código de estado proporciona información sobre la respuesta y ayuda a la aplicación cliente a saber de qué tipo de respuesta se trata.

| Rango    | Información   |
|----------|----------|
| 1xx      | Respuesta informativa         |
| 2xx      | Operación ejecutada con éxito  | 
| 3xx      | Redirección   |
| 4xx      | Error en el cliente/peticion                |
| 5xx      | Error en el servidor                |

#### Documentación de una API

Normalmente cualquier API permitirá consultar su documentación para saber a qué **endpoints** se puede pueden enviar peticiones, qué tipo de peticiones se pueden enviar, con qué parámetros y funcionalidad tienen.

Los **endpoints** de la API son las URL públicas expuestas por el servidor que una API y que el cliente utiliza para acceder a recursos y datos.

| HTTP method	| API endpoint	| Description |
|---------------|---------------|-------------|
|GET   |/products |	Get a list of products.|
|GET	   |/products?limit=x |	Get only x products.|
|GET	| /products/<product_id> |	Get a single product.|
|POST |	/products |	Create a new product.|
|PUT |	/products/<product_id> |	Update a product.|
|PATCH |	/products/<product_id> |	Partially update a product.|
|DELETE	|/products/<product_id>	| Delete a product.|

La URL de la API es https://fakestoreapi.com

#### Primera petición a una API

```python
import requests

r = requests
```







**[Siguiente](../18_WebScrapping/README.md)**
