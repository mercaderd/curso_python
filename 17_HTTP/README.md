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

#### Cuerpo - Payload

La parte final de la petición el el cuerpo, es el contenido de la petición. No todas las peticiones llevan uno: las peticiones que reclaman datos, como GET, normalmente no necesitan ningún cuerpo. Las peticiones que envían datos, como POST, normalmente siempre llevan un cuerpo.
El cuerpo de la petición puede ser datos en formato JSON, puede ser una imágen, cualquier tipo de archivo, ...

### Respuestas HTTP - Responses




## APIs

## API REST




**[Siguiente](../18_WebScrapping/README.md)**
