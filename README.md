# 🛒 E-Commerce App

A full-stack e-commerce web application built with Django. Users can browse products, manage a shopping cart, and place orders. Includes admin features for product management. Yet still work in progress

## ✨ Features

- Product browsing
- Shopping cart functionality
- Order checkout process
- Admin panel for managing products and users

## ⚙️ Tech Stack

- **Backend:** Python 3.x, Django
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Database:** SQLite (default, easy to switch to PostgreSQL)
- **Other:** Django admin panel, Django templating system

## 📁 Project Structure
```
│   .gitignore
│   db.sqlite3
│   manage.py
│   requirements.txt
│
├───ecommerce
│       asgi.py
│       settings.py
│       urls.py
│       wsgi.py
│       __init__.py
│
├───static
│   ├───css
│   │       main.css
│   │
│   ├───images
│   │       arrow-down.png
│   │       arrow-up.png
│   │       book.jpg
│   │       book_tKMjWJz.jpg
│   │       cart.png
│   │       headphones.jpg
│   │       placeholder.png
│   │       shirt.jpg
│   │       shoes.jpg
│   │       sourcecode.jpg
│   │       watch.jpg
│   │
│   └───js
│           cart.js
│
└───store
    │   admin.py
    │   apps.py
    │   models.py
    │   tests.py
    │   urls.py
    │   utils.py
    │   views.py
    │   __init__.py
    │
    ├───migrations
    │
    └───templates
        └───store
                cart.html
                checkout.html
                main.html
                store.html

```


## 🚀 Getting Started

1. **Clone the repository:**

```bash
git clone https://github.com/Kubas052/e-commerce-app.git
cd e-commerce-app
```
2. **Create and activate a virtual environment:**
```
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```
3. **Install dependencies:**
```
pip install -r requirements.txt
```
4. **Apply migrations and start the development server:**
```
python manage.py migrate
python manage.py runserver
```
5. **Create a superuser (admin account):**
```
python manage.py createsuperuser
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
