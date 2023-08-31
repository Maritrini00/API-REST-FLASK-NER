# API Rest para el reconocimiento de entidades nombradas con Phyton.

Objetivo: Crear una API REST sencilla que reciba una lista de oraciones en español y
devuelva una lista de las entidades nombradas identificadas en cada oración.

## Requisitos

Para hacer uso de esta API se necesitan de las siguientes librerias: spacy, Flask y Jsonify

```bash
pip install spacy flask jsonify
python -m spacy download es_core_news_sm
```
Además se va a requerir de la aplicacion POSTMAN

[descargar postman aquí](https://www.postman.com/downloads/)
## Uso

Una vez que se tenga descargada la aplicación app.py en su computadora, se probará de la siguiente manera:

1. correr la aplicación:  
```bash
python app.py
```
2. Abrir postman en su computadora

3. Crear un nuevo request y escoger el método HTTP "POST"
4. En el campo de URL (cuando la aplicación de Flask está corriendo) se ingrese "http://127.0.0.1:3000/extract_ner"  
5. Se le da click en el tab "Headers" y se le agrega un encabezado "Content-Type" con un valor "application/json"
6 Click al apartado "Body" seleccionando la opción "raw", entonces se ingresa el documento JSON de la siguiente manera:
```JSON
{
"oraciones": [
"Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
"San Francisco considera prohibir los robots de entrega en la acera."
]
}
```