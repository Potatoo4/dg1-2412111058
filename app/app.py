import json
import os

from flask import Flask, jsonify, render_template, request


app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

MSSV = "2412111058"
HOTEN = "Hoàng Đức Anh"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "students.json")

PORT = int(os.getenv("PORT", "5000"))


def read_students():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def write_students(students):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(
            students,
            file,
            ensure_ascii=False,
            indent=2
        )


@app.get("/")
def home():
    students = read_students()

    title = f"DG1 – {HOTEN} – {MSSV}"

    return render_template(
        "index.html",
        title=title,
        students=students
    )


@app.get("/api/health")
def health():
    return jsonify({
        "status": "ok",
        "student": MSSV
    })


@app.get("/api/students")
def get_students():
    students = read_students()

    lop = request.args.get("lop")

    if lop:
        students = [
            student
            for student in students
            if student.get("lop") == lop
        ]

    return jsonify(students)


@app.get("/api/students/<int:student_id>")
def get_student(student_id):
    students = read_students()

    for student in students:
        if student.get("id") == student_id:
            return jsonify(student)

    return jsonify({
        "error": "Student not found"
    }), 404


@app.post("/api/students")
def add_student():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "Request body must be JSON"
        }), 400

    required_fields = [
        "mssv",
        "ho_ten",
        "lop",
        "diem"
    ]

    for field in required_fields:
        if field not in data or data[field] in ("", None):
            return jsonify({
                "error": f"Missing field: {field}"
            }), 400

    try:
        diem = float(data["diem"])
    except (TypeError, ValueError):
        return jsonify({
            "error": "diem must be a number"
        }), 400

    if diem < 0 or diem > 10:
        return jsonify({
            "error": "diem must be between 0 and 10"
        }), 400

    students = read_students()

    if students:
        new_id = max(
            int(student["id"])
            for student in students
        ) + 1
    else:
        new_id = 1

    new_student = {
        "id": new_id,
        "mssv": str(data["mssv"]),
        "ho_ten": str(data["ho_ten"]),
        "lop": str(data["lop"]),
        "diem": diem
    }

    students.append(new_student)

    write_students(students)

    return jsonify(new_student), 201


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=PORT
    )
