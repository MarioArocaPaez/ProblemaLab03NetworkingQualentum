# Problema Lab 03: API REST con Flask

Este proyecto implementa una **API REST semántica** utilizando el framework **Flask** en Python. Expone un servicio con operaciones CRUD (Create, Read, Update, Delete) sobre una base de datos en memoria.

---

## **Descripción del Proyecto**

### **Objetivo**
Diseñar una API REST semántica que permita interactuar con cadenas almacenadas en una base de datos en memoria. La API asigna códigos de respuesta HTTP adecuados para cada caso.

### **Características**
- **Añadir cadenas** (`POST`): Prohíbe duplicados.
- **Leer todas las cadenas** (`GET`).
- **Actualizar cadenas** (`PUT`): Actualiza una cadena existente.
- **Eliminar cadenas** (`DELETE`): Elimina una cadena existente.
- **Control de errores**:
  - No se permiten cadenas duplicadas.
  - No se puede actualizar/borrar cadenas que no existen.

---

## **Estructura del Proyecto**

La estructura del proyecto es la siguiente:

```plaintext
├── app.py            # Código principal del servidor Flask
├── database.py       # Funciones CRUD y base de datos en memoria
├── test_app.py       # Pruebas con pytest
└── README.md         # Documentación
```

## **Requisitos Previos**

1. **Python 3.8+**
2. Instala las dependencias necesarias con pip:

   ```bash
   pip install flask pytest
   ```
Instrucciones para Ejecutar

    Clona el repositorio:

git clone git@github.com:MarioArocaPaez/ProblemaLab03NetworkingQualentum.git cd Problema Lab 03 Networking

Inicia el servidor Flask: Ejecuta el servidor local con:

    python app.py

    El servidor se ejecutará en http://127.0.0.1:5000.

    Endpoints Disponibles:

Método Endpoint Descripción Ejemplo de Uso POST /strings Añadir una
nueva cadena { "string": "hello" } GET /strings Leer todas las cadenas -
PUT /strings/`<old_string>`{=html} Actualizar una cadena { "new_string":
"updated" } DELETE /strings/`<string>`{=html} Eliminar una cadena -
Ejemplos de Respuestas 1. POST /strings

    Éxito:

{"message": "String added"}

Código: 201 Created

Error (cadena duplicada):

    {"error": "String already exists"}

    Código: 400 Bad Request

2.  GET /strings

    Respuesta:

    {"data": \["hello", "world"\]}

    Código: 200 OK

3.  PUT /strings/`<old_string>`{=html}

    Éxito:

{"message": "String updated"}

Código: 200 OK

Error (cadena no encontrada):

    {"error": "String not found"}

    Código: 404 Not Found

4.  DELETE /strings/`<string>`{=html}

    Éxito:

{"message": "String deleted"}

Código: 200 OK

Error (cadena no encontrada):

    {"error": "String not found"}

    Código: 404 Not Found

Pruebas con pytest

Se han implementado pruebas unitarias usando pytest para verificar la
funcionalidad de cada endpoint.

    Ejecuta las pruebas con el siguiente comando:

    pytest test_app.py

    Cobertura de pruebas:
        Prueba de creación (POST /strings).
        Manejo de duplicados.
        Prueba de lectura (GET /strings).
        Prueba de actualización (PUT /strings/<old_string>).
        Prueba de eliminación (DELETE /strings/<string>).
