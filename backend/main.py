from fastapi import FastAPI, Depends, HTTPException
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Student
from schemas import StudentCreate, StudentResponse
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
from fastapi import Request
from fastapi.responses import JSONResponse

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5501"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type"]
)
@app.get("/")
def home():
    return {"message": "Welcome to Student Management System"}


@app.post("/students", response_model=StudentResponse, status_code=201)
def add_student(student: StudentCreate, db: Session = Depends(get_db)):

    existing_student = db.query(Student).filter(
        Student.email == student.email
    ).first()

    if existing_student:
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )

    new_student = Student(
        name=student.name,
        age=student.age,
        email=student.email,
        course=student.course
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


@app.get("/students", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return students


@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student: StudentCreate, db: Session = Depends(get_db)):

    existing_student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if existing_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    duplicate_email = db.query(Student).filter(
        Student.email == student.email,
        Student.id != student_id
    ).first()

    if duplicate_email:
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )

    existing_student.name = student.name
    existing_student.age = student.age
    existing_student.email = student.email
    existing_student.course = student.course

    db.commit()
    db.refresh(existing_student)

    return existing_student


@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()

    return {"message": "Student deleted successfully"}
