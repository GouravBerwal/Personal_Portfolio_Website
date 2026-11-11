# Gourav Berwal - Personal Portfolio Website

A modern, responsive, and dynamic personal portfolio web application built with **Django**, **HTML5**, **CSS3**, and **JavaScript**.

---

## 🌟 Features

- **Dynamic Django Architecture**:
  - Built using standard Django MVT (Model-View-Template) pattern.
  - SQLite database pre-configured and seeded with all skills, projects, and work experiences.
  - Django Admin panel enabled for managing projects, skills, profile details, and viewing contact messages.
- **Modern UI & Responsive Design**:
  - Interactive 3D flip cards on project hover/touch.
  - Dynamic project category filtering (Software Engineering, Machine Learning / AI, Data Analytics).
  - Floating background particles animation in the hero banner.
  - Clean vertical timeline for work experience with company logos.
  - Smooth scroll navigation and responsive mobile navbar.
- **Interactive Contact Form**:
  - Real-time client-side validation.
  - Asynchronous AJAX submission to Django backend with CSRF protection.
  - Messages automatically stored in the database (`ContactMessage` model) and visible in the Admin dashboard.

---

## 📁 Project Directory Structure

```
Portfolio/
├── manage.py                          # Django management script
├── db.sqlite3                         # Pre-seeded SQLite database
├── requirements.txt                   # Project dependencies
├── .gitignore                         # Git ignore configuration
├── README.md                          # Documentation
│
├── portfolio_project/                 # Main Django project package
│   ├── __init__.py
│   ├── settings.py                    # Project settings & static configurations
│   ├── urls.py                        # Root URL router
│   ├── wsgi.py
│   └── asgi.py
│
├── portfolio/                         # Core Portfolio Django app
│   ├── admin.py                       # Admin dashboard registrations
│   ├── apps.py                        # App configuration
│   ├── forms.py                       # Contact form definition
│   ├── models.py                      # Profile, Skill, Project, Experience, ContactMessage
│   ├── urls.py                        # App routes ('', 'contact/')
│   ├── views.py                       # Rendering & form handling views
│   ├── tests.py                       # Unit tests
│   └── management/
│       └── commands/
│           └── seed_portfolio.py      # Data seeding command
│
├── static/                            # Static assets
│   ├── css/
│   │   └── style.css                  # Custom styling
│   ├── js/
│   │   └── main.js                    # Navbar, filter, animations, AJAX contact form
│   └── images/                        # All project images, logos, skill icons, backgrounds
│
├── templates/                         # HTML templates
│   ├── base.html                      # Base layout with navbar, footer, scripts
│   └── index.html                     # Main portfolio page extending base
│
└── media/                             # Uploaded media directory
```

---

## 🚀 How to Run the Project

### 1. Open Terminal in VS Code
Make sure you are in the project folder:
```bash
cd /Users/gurjar/Desktop/Portfolio
```

### 2. Run the Development Server
Run the following command:
```bash
python3 manage.py runserver
```

### 3. Open in Browser
Visit:
- **Portfolio Website**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Django Admin Panel**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🔐 Admin Credentials

A superuser account is already created for you:
- **Username**: `admin`
- **Password**: `admin123`

You can log in at `http://127.0.0.1:8000/admin/` to:
- Add, edit, or reorder **Projects**
- Add or update **Skills**
- Add or update **Work Experience**
- Update your **Profile**, bio, and social links
- View incoming **Contact Messages** submitted through your portfolio!

---

## 🔄 Re-seeding Data (If needed)

If you ever reset the database or want to re-seed the default data:
```bash
python3 manage.py migrate
python3 manage.py seed_portfolio
```

---

## 🧪 Running Tests

To verify that all views and form submissions are functioning properly:
```bash
python3 manage.py test
```
