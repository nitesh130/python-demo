from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/employee/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    # Hardcoded employee data
    employees = {
        1: {"id": 1, "name": "John Doe", "role": "Software Engineer"},
        2: {"id": 2, "name": "Jane Smith", "role": "Project Manager"},
        3: {"id": 3, "name": "Alice Johnson", "role": "Designer"}
    }
    employee = employees.get(employee_id, {"id": 0, "name": "Unknown", "role": "Unknown"})
    return jsonify(employee)


if __name__ == '__main__':
    app.run(debug=True)