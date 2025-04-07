# 📝 Django Blog

A fully featured and modular blog backend built with **Django** and **Django REST Framework**, designed for scalable API development. This project includes robust user authentication with JWT, password reset via SMS, token blacklisting, and complete blog post CRUD functionalities. Ideal for learning or extending into a full production system.



---

## 🚀 Features

- 🔐 JWT-based user authentication (Login & Register)  
- 📲 Password reset via phone number and SMS verification code  
- 🔁 Token blacklisting on logout  
- 📝 CRUD operations for blog posts (Create, Read, Update, Delete)  
- 🛡️ Secure password hashing and reset flow  
- 🧩 Fully customizable and extendable architecture  
- 🔧 Django admin panel for managing users and content

---

## 🧰 Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=jsonwebtokens&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" />
  
---

## 📦 Installation & Setup

Follow the steps below to set up the project locally:

### 1. 📁 Clone the repository
```bash
git clone git@github.com:USERNAME/PROJECT_NAME.git
cd django_blog
```

### 2. 🐍 Create a virtual environment
It’s recommended to use a virtual environment to isolate dependencies.

```bash
# Create virtual environment

python -m venv venv

# Activate the virtual environment

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. 📦 Install project dependencies
```bash
pip install --upgrade pip

pip install -r requirements.txt
```

### 4. ⚙️ Apply database migrations
```bash
python manage.py makemigrations

python manage.py migrate
```

### 5. 🔐 Create a superuser (for accessing the admin panel)
```bash
python manage.py createsuperuser
```

### 6. 🚀 Run the development server
```bash
python manage.py runserver
```

Visit the app at [http://127.0.0.1:8000](http://127.0.0.1:8000) 
 
Visit the admin panel at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)



---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## 🧩 Mockup Demo Sketch

```
+--------------------------------------------------------------+
|                         Django Blogify                       |
|         A Modular Blog Backend with JWT Auth & SMS          |
+-------------------+        DRF        +----------------------+
|                   |------------------>|                      |
|   📦 Account App  |                   |  ✍️ Blogging App      |
|-------------------|                  |----------------------|
| 🔐 Register       |                  | 📝 Create Post        |
| 🔑 Login          |                  | 📖 Read Post          |
| 🚪 Logout         |                  | 🛠️ Update Post        |
| 📲 SMS Reset Code |                  | ❌ Delete Post        |
| 🔁 Change Pass    |                  |                      |
+-------------------+        ⬇️        +----------------------+
                        🔑 JWT Token System
                        Access + Refresh Tokens
                        🧹 Token Blacklisting on Logout
```

---