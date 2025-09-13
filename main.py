from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, PositiveInt
from typing import Optional, List  # Corrected: Optional imported from typing, not Pydantic

# Step 1: Define Pydantic Data Models for Validation
class StudentCreate(BaseModel):
    name: str
    age: PositiveInt  # Ensures age is a positive integer
    gender: str
    email: EmailStr  # Validates email format (e.g., user@domain.com)

class StudentUpdate(BaseModel):
    name: Optional[str] = None    # Optional field (can be omitted)
    age: Optional[PositiveInt] = None  # Optional positive integer
    gender: Optional[str] = None  # Optional field
    email: Optional[EmailStr] = None   # Optional valid email

class Student(StudentCreate):
    id: int  # Unique student ID (auto-generated)

# Step 2: Initialize FastAPI App and In-Memory Storage
app = FastAPI()
students: List[Student] = []  # Stores student records
next_id = 1  # Tracks the next available student ID

# Step 3: Implement API Endpoints
## Add a Student (POST /students)
@app.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED)
async def create_student(student: StudentCreate):
    global next_id, students
    new_student = Student(id=next_id, **student.dict())  # Auto-generate ID
    students.append(new_student)
    next_id += 1  # Increment ID for next student
    return new_student

## Get All Students (GET /students)
@app.get("/students", response_model=List[Student])
async def get_all_students():
    return students

## Get Student by ID (GET /students/{student_id})
@app.get("/students/{student_id}", response_model=Student)
async def get_student(student_id: int):
    print(f"[DEBUG] Searching for student ID: {student_id}")  # Print the ID being searched
    print(f"[DEBUG] Current students list: {students}")       # Print the entire list (for verification)
    student = next((s for s in students if s.id == student_id), None)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    print(f"[DEBUG] Found student: {student}")  # Print the found student (if any)
    return student

## Update a Student (PUT /students/{student_id})
@app.put("/students/{student_id}", response_model=Student)
async def update_student(student_id: int, updated_student: StudentUpdate):
    global students
    # Find index of the student by ID
    index = next((i for i, s in enumerate(students) if s.id == student_id), None)
    if index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    current_student = students[index]  # Get current student data
    # Update fields if provided (skip "None" values)
    update_data = updated_student.dict(exclude_unset=True)  # Exclude fields not in the request
    current_student_data = current_student.dict()  # Convert current student to dict
    current_student_data.update(update_data)  # Merge with new data
    # Create updated Student (triggers Pydantic validation)
    updated_student_obj = Student(**current_student_data)
    students[index] = updated_student_obj  # Replace old student with updated one
    return updated_student_obj

## Delete a Student (DELETE /students/{student_id})
@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_student(student_id: int):
    global students
    index = next((i for i, s in enumerate(students) if s.id == student_id), None)
    if index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    del students[index]  # Remove student from the list