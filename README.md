<div align="center">

# 🌐 Gourav Berwal — Personal Portfolio Website

### *Modern • Responsive • Data-Driven Full-Stack Web Application*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Responsive](https://img.shields.io/badge/Responsive-Mobile_S_to_4K-4B8BBE?style=for-the-badge&logo=responsive&logoColor=white)](#-multi-device-responsive-matrix)
[![Status](https://img.shields.io/badge/Status-Production_Ready-success?style=for-the-badge)](#)

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/gouravberwal/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat-square&logo=github)](https://github.com/GouravBerwal)
[![LeetCode](https://img.shields.io/badge/LeetCode-Profile-FFA116?style=flat-square&logo=leetcode)](https://leetcode.com/)
[![Gmail](https://img.shields.io/badge/Gmail-Contact-EA4335?style=flat-square&logo=gmail)](mailto:gouravberwal003@gmail.com)

---

</div>

## 📖 Overview

An enterprise-grade, fully responsive, and dynamic personal portfolio web application engineered with **Python**, **Django**, semantic **HTML5**, modern fluid **CSS3**, and vanilla **JavaScript (ES6+)**. 

Designed with Apple-inspired minimalism, deep oceanic navy aesthetics, dynamic 3D interactive flip cards, and FAANG-grade technical bullet points, this platform showcases full-stack software development expertise, data analytics capabilities, and verified professional engineering experience.

---

## 🌟 Key Architecture & Highlights

### 🎨 Apple-Inspired Design & UI
- **Oceanic Navy Sky Hero**: Subtle gradient overlay with floating canvas bokeh particles, custom typography via Google Fonts (`Montserrat`, `Source Sans Pro`), and glowing cyan-teal avatar accents.
- **3D Interactive Flip Project Cards**: Hardware-accelerated CSS 3D card flips (`preserve-3d`, `rotateY(180deg)`) revealing technical bullet points, tech stack tags, and direct repository links.
- **Touch-Safe UX**: Mobile-first touch interactions with visible tap-to-flip pill badges and link-propagation shielding so tapping repository links doesn't trigger accidental flips.
- **Glassmorphism Navigation**: Floating sticky navigation bar with backdrop blur filter, active scroll section tracking, and responsive mobile sliding drawer with background scroll lock.

### ⚡ Dynamic Django Backend (MVT Architecture)
- **Decoupled Relational Models**:
  - `Profile`: Centralized bio, contact, avatar, and social handle configurations.
  - `Skill`: Categorized technical competencies with custom SVG/PNG brand icon mapping.
  - `Project`: Project showcase engine with live URL, repository URL, tech tags, and 3-tier impact bullets.
  - `Experience`: Chronological work experience timeline with company logos and responsibilities.
  - `ContactMessage`: Persisted visitor inquiries with timestamp and read/unread flags.
- **Django Admin CMS**: Full administrative dashboard to manage, update, and reorder content without editing templates or deploying code changes.
- **One-Command Database Seeding**: Pre-built management command (`python manage.py seed_portfolio`) to instantly restore or initialize sample data.

### 📱 Full Multi-Tier Device Responsiveness
- Engineered from the ground up using CSS `clamp()` and scalable rem units.
- Seamless presentation across all screen dimensions without requiring browser zoom:
  - **Mobile S** (320px – 360px)
  - **Mobile M & L** (375px – 480px)
  - **Tablets & iPads** (481px – 991px)
  - **Laptops & Desktops** (992px – 1920px)
  - **4K Ultra-HD & Studio Displays** (2000px – 3840px+)

### 📄 Integrated Native Resume Engine
- Native `/resume/` endpoint serving high-fidelity PDF documents inline directly within the browser viewer without external third-party redirects.
- Direct attachment download support via `?download=1` query parameter (`Content-Disposition: attachment; filename="Gourav_Berwal_Resume.pdf"`).

### ✉️ Secure Asynchronous Contact Pipeline
- Real-time client-side input validation with custom animated error hints.
- Asynchronous **AJAX submission** with Django CSRF protection, returning instant JSON status feedback without full page reloads.

### 🛡️ Production-Ready Security & Configuration
- Decoupled sensitive settings using environment variables (`DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, `DJANGO_ALLOWED_HOSTS`).
- Local SQLite database and environment secrets excluded from version control via strictly configured `.gitignore`.

---

## 📱 Multi-Device Responsive Matrix

| Breakpoint Tier | Viewport Width | Layout & Adaptations |
| :--- | :--- | :--- |
| **Mobile S** | `320px – 360px` | 12px safe margins, 2-column skills grid, 1-column project cards (410px height), single vertical timeline spine with compact nodes, touch-flip pill badge. |
| **Mobile M & L** | `361px – 480px` | Fluid typography, 2-column skills with 50px icons, 1-column project cards, full-width touch-friendly form buttons (48px height). |
| **Tablets** | `481px – 991px` | Glassmorphic slide-out drawer menu with body scroll lock, 3-column skills, 2-column project cards, side-by-side about layout. |
| **Laptops & Desktops** | `992px – 1920px` | 1440px max fluid container, 3-column project grid with 3D hover flip, alternating zigzag experience timeline with pulsing company nodes. |
| **4K Ultra-HD** | `2000px – 3840px+` | Root scale adjustment (`19px`), 1800px max container, 4-column project grid (420px height), 6-column skills layout. |

---

## 🛠️ Tech Stack & Tools

| Layer | Technologies & Libraries |
| :--- | :--- |
| **Backend Framework** | [Python 3.10+](https://www.python.org/) • [Django 5.x](https://www.djangoproject.com/) |
| **Database** | SQLite (Development) / PostgreSQL & MySQL Ready |
| **Frontend UI** | HTML5 Semantic Markup • CSS3 Modern Flexbox & Grid • Vanilla JavaScript (ES6+) |
| **Icons & Typography** | [Font Awesome 6](https://fontawesome.com/) • [Bootstrap Icons](https://icons.getbootstrap.com/) • Google Fonts (`Montserrat`, `Source Sans Pro`) |
| **Design Paradigm** | Responsive Web Design (RWD) • Mobile-First • Glassmorphism • CSS 3D Transforms |
| **DevOps & Tools** | Git • GitHub • VS Code • Virtualenv |

---

## 📁 Directory Architecture

```
Personal_Portfolio_Website/
├── manage.py                          # Django management CLI
├── requirements.txt                   # Production & development dependencies
├── .gitignore                         # Version control exclusions
├── .env.example                       # Environment variables template
├── README.md                          # Repository documentation
│
├── portfolio_project/                 # Django project configuration
│   ├── __init__.py
│   ├── settings.py                    # Settings with environment variable support
│   ├── urls.py                        # Root URL routing
│   ├── wsgi.py                        # WSGI entry point
│   └── asgi.py                        # ASGI entry point
│
├── portfolio/                         # Core portfolio Django application
│   ├── admin.py                       # Django Admin configuration & list displays
│   ├── apps.py                        # App metadata
│   ├── forms.py                       # ContactForm definition
│   ├── models.py                      # Profile, Skill, Project, Experience, ContactMessage
│   ├── urls.py                        # Application routes ('', 'resume/', 'contact/')
│   ├── views.py                       # View controllers & PDF streaming response
│   ├── tests.py                       # Comprehensive unit test suite
│   ├── migrations/                    # Database schema migration history
│   └── management/
│       └── commands/
│           └── seed_portfolio.py      # Automated database population command
│
├── static/                            # Static asset pipeline
│   ├── css/
│   │   └── style.css                  # Custom responsive design system
│   ├── js/
│   │   └── main.js                    # Mobile drawer, particles, filtering, AJAX logic
│   ├── docs/
│   │   └── Gourav_Berwal_Resume.pdf   # Native resume PDF
│   └── images/                        # Project screenshots, company logos, skill SVGs
│
└── templates/                         # Django HTML templates
    ├── base.html                      # Root layout, navigation drawer, footer
    └── index.html                     # Single-page portfolio template
```

---

## 🚀 Quick Start / Local Setup

Follow these steps to run the portfolio website locally on your machine:

### 1. Clone the Repository
```bash
git clone https://github.com/GouravBerwal/Personal_Portfolio_Website.git
cd Personal_Portfolio_Website
```

### 2. Create and Activate a Virtual Environment
```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows (Command Prompt / PowerShell)
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables (Optional)
You can optionally create a `.env` file from the provided `.env.example`:
```bash
cp .env.example .env
```

### 5. Run Database Migrations
Initialize your local database schema:
```bash
python3 manage.py migrate
```

### 6. Seed the Portfolio Data
Populate the database with all skills, projects, work experience, and profile content:
```bash
python3 manage.py seed_portfolio
```

### 7. Create an Admin User (Optional)
To manage content via the Django Admin panel:
```bash
python3 manage.py createsuperuser
```
*(Follow the interactive prompts to set your own secure username, email, and password).*

### 8. Start the Development Server
```bash
python3 manage.py runserver
```

Open your browser and visit:
- **Portfolio Website**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Django Admin Dashboard**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- **Native Resume Viewer**: [http://127.0.0.1:8000/resume/](http://127.0.0.1:8000/resume/)

---

## 🧪 Running Unit Tests

Execute the automated test suite to verify route resolution, page rendering, form handling, and PDF serving:
```bash
python3 manage.py test portfolio
```

---

## ⚙️ Environment Variables Reference

| Variable | Default Value | Description |
| :--- | :--- | :--- |
| `DJANGO_SECRET_KEY` | Development default | Cryptographic signing key. Set a secure random string in production. |
| `DJANGO_DEBUG` | `True` | Set to `False` in live production environments. |
| `DJANGO_ALLOWED_HOSTS` | `*` | Comma-separated list of allowed domains / IP addresses. |

---

## 👨‍💻 Author

**Gourav Berwal**  
*Computer Science & Engineering Student @ CGC University, Mohali*  
*Python Developer Intern @ Alphawizz Technologies Pvt. Ltd*

- **LinkedIn**: [linkedin.com/in/gouravberwal](https://www.linkedin.com/in/gouravberwal/)
- **GitHub**: [github.com/GouravBerwal](https://github.com/GouravBerwal)
- **Email**: [gouravberwal003@gmail.com](mailto:gouravberwal003@gmail.com)

---

## 📜 License

This project is open-source and available under the **[MIT License](LICENSE)**. Feel free to use it as inspiration or a template for your own developer portfolio!
