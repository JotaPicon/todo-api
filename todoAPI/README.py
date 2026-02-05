# To-Do API con Flask

API REST sencilla para gestionar tareas pendientes.

## Tecnologías
- Python 3
- Flask

## Funcionalidades
- Listar tareas (`GET /tasks`)
- Obtener tarea por ID (`GET /tasks/<id>`)
- Crear tarea (`POST /tasks`)
- Actualizar tarea (`PUT /tasks/<id>`)
- Eliminar tarea (`DELETE /tasks/<id>`)

## Instalación
1. Clonar el repositorio
2. Instalar dependencias: `pip install -r requirements.txt`
3. Ejecutar: `python app.py`
4. Acceder en: `http://localhost:5000/tasks`