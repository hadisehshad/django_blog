# ?? Django Blogify

A fully featured and modular blog backend built with **Django** and **Django REST Framework**, designed for scalable API development. This project includes robust user authentication with JWT, password reset via SMS, token blacklisting, and complete blog post CRUD functionalities. Ideal for learning or extending into a full production system.

---

## ?? Features

?- JWT-based user authentication (Login & Register)
??- Password reset via phone number and SMS verification code
??- Token blacklisting on logout
??- CRUD operations for blog posts (Create, Read, Update,              Delete)
???- Secure password hashing and reset flow
??- Fully customizable and extendable architecture
??- Django admin panel for managing users and content

---

## ?? Installation

 **Clone the repository**

```bash
git clone git@github.com:USERNAME/PROJECT_NAME.git

cd django_blog


?? Admin Panel Access

Visit: http://127.0.0.1:8000/admin/
Login with your superuser credentials created earlie

?? License
This project is licensed under the MIT License.


?? Mockup Demo Sketch

+--------------------------------------------------------------+
|                         Django Blogify                       |
|         A Modular Blog Backend with JWT Auth & SMS          |
+-------------------+        DRF        +----------------------+
|                   |------------------>|                      |
|   ?? Account App  |                   |  ?? Blogging App      |
|-------------------|                  |----------------------|
| ?? Register       |                  | ?? Create Post        |
| ?? Login          |                  | ?? Read Post          |
| ?? Logout         |                  | ??? Update Post        |
| ?? SMS Reset Code |                  | ? Delete Post        |
| ?? Change Pass    |                  |                      |
+-------------------+        ??        +----------------------+
                        ?? JWT Token System
                        Access + Refresh Tokens
                        ?? Token Blacklisting on Logout
