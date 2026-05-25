
# **🚀 Django REST Framework CRUD Operation**

A powerful **Student Management REST API** built using **Python, Django, Django REST Framework, and MySQL**. This project demonstrates complete **CRUD (Create, Read, Update, Delete)** operations with proper validation, API handling, and database integration.

---

# **✨ Features**

✅ Create Student Record  
✅ View All Student Records  
✅ View Single Student Details  
✅ Update Student Information  
✅ Delete Student Record  
✅ Input Validation  
✅ Unique Email & Mobile Validation  
✅ MySQL Database Integration  
✅ REST API Development  
✅ Postman API Testing  
✅ Error Handling  

---

# **🛠️ Tech Stack**

- **Python**
- **Django**
- **Django REST Framework**
- **MySQL**
- **Postman**
- **Git**
- **GitHub**

---

# **📂 Project Structure**

```bash
RestCrud/
│── Crud/
│   │── settings.py
│   │── urls.py
│── Rest_Crud/
│   │── models.py
│   │── serializers.py
│   │── views.py
│   │── urls.py
│── manage.py
│── requirements.txt
```

---

# **📌 API Endpoints**

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /student/create/ | Create student |
| GET | /student/list/ | Get all students |
| GET | /student/detail/<id>/ | Get single student |
| PUT | /student/update/<id>/ | Update student |
| DELETE | /student/delete/<id>/ | Delete student |

---

# **📥 Installation Guide**

## **📂 Clone Repository**

```bash
git clone https://github.com/your-username/your-repository-name.git
```

## **📁 Move to Project Folder**

```bash
cd your-repository-name
```

## **🐍 Create Virtual Environment**

```bash
python -m venv env
```

## **⚡ Activate Virtual Environment**

**Windows**
```bash
env\Scripts\activate
```

**Mac/Linux**
```bash
source env/bin/activate
```

## **📦 Install Dependencies**

```bash
pip install -r requirements.txt
```

## **🗄️ Configure Database**

Update your **settings.py**

```python
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
```

## **🔄 Run Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

## **🚀 Start Server**

```bash
python manage.py runserver
```

---

# **🧪 API Testing with Postman**

Use Postman to test API endpoints.

Example:

```bash
http://127.0.0.1:8000/student/list/
```

---

# **📮 API Request Examples**

## **➕ Create Student (POST)**

```bash
http://127.0.0.1:8000/student/create/
```

**Request Body**
```json
{
    "name": "Dharshan",
    "age": 22,
    "course": "Python Django",
    "email": "dharshan@example.com",
    "mobile": "9876543210"
}
```

---

## **📋 Get All Students (GET)**

```bash
http://127.0.0.1:8000/student/list/
```

---

## **🔍 Get Student By ID (GET)**

```bash
http://127.0.0.1:8000/student/detail/1/
```

---

## **✏️ Update Student (PUT)**

```bash
http://127.0.0.1:8000/student/update/1/
```

**Request Body**
```json
{
    "name": "Dharshan Updated",
    "age": 23,
    "course": "Django REST Framework",
    "email": "dharshanupdated@example.com",
    "mobile": "9876543211"
}
```

---

## **🗑️ Delete Student (DELETE)**

```bash
http://127.0.0.1:8000/student/delete/1/
```

---

# **📸 Sample JSON Request**

```json
{
    "name": "Dharshan",
    "age": 22,
    "course": "Python Django",
    "email": "dharshan@example.com",
    "mobile": "9876543210"
}
```

---

# **🎯 Learning Outcomes**

This project helped me understand:

- **Django REST Framework API Development**
- **CRUD Operations**
- **Serializer Validation**
- **Database Integration with MySQL**
- **API Testing using Postman**
- **Error Handling**
- **GitHub Project Management**

---

# **🤝 Contributing**

Contributions are welcome! Feel free to fork this repository and submit pull requests.

---

# **📜 License**

This project is open-source and available under the **MIT License**.

---

# **⭐ Support**

If you like this project, please **Star ⭐ this repository**.

---

# CRUD Operation Post Method 

<img width="1920" height="1080" alt="Screenshot 2026-05-25 112300" src="https://github.com/user-attachments/assets/c491ff52-213d-47b1-8f8c-d867ccef5e49" />

---

# Get Method all Data 

<img width="1920" height="1080" alt="Screenshot 2026-05-25 112350" src="https://github.com/user-attachments/assets/cb8c2ce9-3196-4d4c-8dd7-13c3e39f45ba" />

---

# GetByid One data only using Id

<img width="1920" height="1080" alt="Screenshot 2026-05-25 112700" src="https://github.com/user-attachments/assets/18a34ed3-3ed1-410e-884d-ccdaada1e904" />

---

# Updat Data using Put Method

<img width="1920" height="1080" alt="Screenshot 2026-05-25 113832" src="https://github.com/user-attachments/assets/a26b8e0d-56d6-4110-b051-06736b727a13" />

---

# Update Data Using Patch Method

<img width="1920" height="1080" alt="Screenshot 2026-05-25 113911" src="https://github.com/user-attachments/assets/a5bc6e71-c052-4aa7-bb3b-bb2d8ec74ba3" />


---

# Delete method 

<img width="1920" height="1080" alt="Screenshot 2026-05-25 113933" src="https://github.com/user-attachments/assets/59f59ac1-21a2-4716-bbd2-d44e460e2918" />

