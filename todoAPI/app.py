from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de tareas en memoria (simulación de base de datos)
tasks = [
    {"id": 1, "title": "Aprender Flask", "done": False},
    {"id": 2, "title": "Subir proyecto a GitHub", "done": False}
]

# Obtener todas las tareas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Obtener una tarea por ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    return jsonify(task) if task else ("Tarea no encontrada", 404)

# Crear nueva tarea
@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = {
        "id": len(tasks) + 1,
        "title": request.json.get("title"),
        "done": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# Actualizar tarea
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return ("Tarea no encontrada", 404)
    task["title"] = request.json.get("title", task["title"])
    task["done"] = request.json.get("done", task["done"])
    return jsonify(task)

# Eliminar tarea
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return ("", 204)

if __name__ == '__main__':
    app.run(debug=True)