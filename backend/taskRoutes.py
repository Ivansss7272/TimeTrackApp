from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from task_controller import create_task, get_tasks, update_task, delete_task

load_dotenv()

app = Flask(__name__)

@app.route('/tasks', methods=['POST'])
def create_task_route():
    task_data = request.json
    result = create_task(task_data)
    return jsonify(result), 201

@app.route('/tasks', methods=['GET'])
def get_tasks_route():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    tasks = get_tasks(start_date, end_date)
    return jsonify(tasks), 200

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task_route(task_id):
    update_data = request.json
    result = update_task(task_id, update_data)
    if result:
        return jsonify(result), 200
    else:
        return jsonify({"error": "Task not found."}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task_route(task_id):
    result = delete_task(task_id)
    if result:
        return jsonify({"message": "Task deleted successfully."}), 200
    else:
        return jsonify({"error": "Task not found."}), 404

if __name__ == '__main__':
    app.run(host=os.getenv('HOST', '127.0.0.1'), port=int(os.getenv('PORT', 5000)))