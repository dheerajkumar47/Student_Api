Student Management API 🎓
A straightforward, in-memory Student Management API built using FastAPI. It's designed to showcase basic CRUD (Create, Read, Update, Delete) operations without needing a database, making it perfect for learning or quick prototyping.

🌟 Key Features
RESTful CRUD Operations: Easily manage student records via a clean, RESTful API.

Built with FastAPI: Take advantage of FastAPI's high performance and automatic interactive API documentation.

Pydantic Data Validation: Ensure data integrity with robust validation for fields like name, age, and email.

In-Memory Storage: Simple to run and test since no external database is required.

📁 Project Structure
student_api/
├── main.py            # Main FastAPI application with all API endpoints
├── requirements.txt   # Project dependencies
└── venv/              # Python virtual environment (recommended)
🚀 Getting Started
Prerequisites
Make sure you have Python 3.8+ and pip installed.

Installation & Setup
Clone the repository:

Bash

git clone https://github.com/your-github-username/student_api.git
cd student_api
Create and activate a virtual environment (recommended):

On macOS/Linux:

Bash

python3 -m venv venv
source venv/bin/activate
On Windows (PowerShell):

Bash

python -m venv venv
.\venv\Scripts\Activate.ps1
Install the required dependencies:

Bash

pip install -r requirements.txt
Run the application:

Bash

uvicorn main:app --reload
The API will now be running locally at http://127.0.0.1:8000.

📖 API Documentation
Once the server is running, you can access the interactive API documentation (powered by Swagger UI) at:

http://127.0.0.1:8000/docs

This is the best way to explore and test the endpoints directly from your browser.

🧪 Testing the Endpoints
Here are some examples of the main API endpoints you can use. You can test these using the interactive docs or a tool like cURL or Postman.

1. Create a Student (POST /students)
Request Body:

JSON

{
  "name": "New Student",
  "age": 20,
  "gender": "Other",
  "email": "new.student@example.com"
}
Response: A 201 Created status code and the created student's data, including a new id.

2. Get All Students (GET /students)
Response: A 200 OK status code with a JSON array of all student records.

3. Get Student by ID (GET /students/{student_id})
Example: GET http://127.0.0.1:8000/students/1

Response: A 200 OK status code with the JSON data for the student with the specified id.

4. Update a Student (PUT /students/{student_id})
Example: PUT http://127.0.0.1:8000/students/1

Request Body:

JSON

{
  "age": 21,
  "email": "updated.student@example.com"
}
Response: A 200 OK status code and the updated student's data.

5. Delete a Student (DELETE /students/{student_id})
Example: DELETE http://127.0.0.1:8000/students/1

Response: A 204 No Content status code upon successful deletion.
