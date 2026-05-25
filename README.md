# 🚀 Django REST Framework CRUD Operation

A powerful and beginner-friendly **Student Management REST API** built using **Python, Django, Django REST Framework, and MySQL**. This project demonstrates complete CRUD (Create, Read, Update, Delete) operations with clean API design, validation, and database integration.

## ✨ Features

✅ Create new student records  
✅ Retrieve all student details  
✅ Retrieve single student by ID  
✅ Update existing student information  
✅ Delete student records  
✅ Input validation and error handling  
✅ Unique field validation (Email / Mobile)  
✅ RESTful API architecture  
✅ MySQL database integration  
✅ API testing with Postman  

---

## 🛠️ Tech Stack

- **Python**
- **Django**
- **Django REST Framework**
- **MySQL**
- **Postman**
- **Git & GitHub**

---

## 📂 Project Structure

```bash
Rest_Crud/
│── Crud/
│   │── settings.py
│   │── urls.py
|   │── __init__.py
|   │── asgi.py
|   │── wsgi.py
│── Restcrud/
│   │── models.py
|   │── admin.py
|   │── apps.py
|   │── test.py
|   │── __init__.py
│   │── serializers.py
│   │── views.py
│   │── urls.py
│── manage.py


---

## Installation
 
Clone Repository
git clone https://github.com/your-username/your-repository-name.git
Move to Project Folder
cd your-repository-name
Create Virtual Environment
python -m venv env
Activate Virtual Environment

---

Windows

env\Scripts\activate

Mac/Linux

source env/bin/activate
Install Dependencies
pip install -r requirements.txt
Configure Database

## Update your settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

Run Migrations
python manage.py makemigrations
python manage.py migrate
Start Server
python manage.py runserver
🧪 Testing API

Use Postman to test API endpoints.

Example:

http://127.0.0.1:8000/student/list/
📸 Sample JSON Request
{
    "name": "Dharshan",
    "age": 22,
    "course": "Python Django",
    "email": "dharshan@example.com",
    "mobile": "9876543210"
}
## 🎯 Learning Outcomes

This project helped me understand:

Django REST Framework API development
CRUD operations implementation
Serializer validation
Database connectivity with MySQL
API testing using Postman
Error handling in REST APIs
GitHub project management


## Post Data In 






