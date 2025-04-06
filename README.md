# 📝 Django Blogify

A fully featured and modular blog backend built with **Django** and **Django REST Framework**, designed for scalable API development. This project includes robust user authentication with JWT, password reset via SMS, token blacklisting, and complete blog post CRUD functionalities. Ideal for learning or extending into a full production system.

---

<p align="center">
  <img src="https://img.shields.io/github/license/hadisehshad/django_blog?style=for-the-badge" />
  <img src="https://img.shields.io/github/stars/hadisehshad/django_blog?style=for-the-badge" />
  <img src="https://img.shields.io/github/forks/hadisehshad/django_blog?style=for-the-badge" />
  <img src="https://img.shields.io/github/last-commit/hadisehshad/django_blog?style=for-the-badge" />
</p>

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
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=jsonwebtokens&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/REST API-005571?style=for-the-badge&logo=fastapi&logoColor=white" />
</p>

---

## 📦 Installation

**Clone the repository**

```bash
git clone https://github.com/hadisehshad/django_blog.git
cd django_blog
```

---

## 🔐 Admin Panel Access

Visit: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)  
Login with your superuser credentials.

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