# APKWeb Django Platform

Welcome to **APKWeb**, a robust Django-based platform designed for seamless management of registrations, insurance, campaigns, and more. This project is built with scalability, modularity, and developer productivity in mind.

---

## 🚀 Features

- **User Registration & Authentication**  
  Secure and flexible user onboarding.

- **Comprehensive Insurance Modules**  
  Manage Life, Health, Motor, Fire, Marine, Liability, and Accident insurance with ease.

- **Campaign Management**  
  Launch, monitor, and cap campaigns with integrated points and rewards.

- **Contact & Complaint Handling**  
  Built-in forms for user feedback and support.

- **Admin Dashboard**  
  Powerful Django admin for all backend operations.

- **Media & Static File Management**  
  Organized handling of user uploads and static assets.

- **Ready for Docker & CI/CD**  
  Effortless deployment and continuous integration with Docker and GitHub Actions.

---

## 🛠️ Tech Stack

- **Backend:** Django 3.1+
- **Database:** SQLite (default, easy to switch)
- **Frontend:** Django Templates (customizable)
- **Containerization:** Docker, Docker Compose
- **CI/CD:** GitHub Actions

---

## ⚡ Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/apkweb-main.git
cd apkweb-main
```

### 2. Local Development

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # Optional, for admin access
python manage.py runserver
```

Visit [http://localhost:8000](http://localhost:8000) to explore the app.

---

## 🐳 Dockerized Development

### 1. Build & Run with Docker Compose

```bash
docker-compose up --build
```

- App runs at [http://localhost:8000](http://localhost:8000)
- Static files: `/assets`
- Media uploads: `/media`

### 2. Environment Variables

Configure sensitive settings via `docker-compose.yml`:

```yaml
environment:
  - DEBUG=True
  - SECRET_KEY=your-secret-key
  - EMAIL_HOST=your-smtp-host
  - EMAIL_PORT=465
  - EMAIL_HOST_USER=your-email
  - EMAIL_HOST_PASSWORD=your-password
  - EMAIL_USE_SSL=True
```

---

## 🔄 Continuous Integration & Deployment

- **CI/CD Pipeline:**  
  Automated with GitHub Actions (`.github/workflows/django-ci-cd.yml`):
  - Installs dependencies
  - Runs migrations and collects static files
  - Executes tests
  - Ready for deployment steps

---

## 📁 Project Structure

```
apkweb-main/
├── apkshopee/
├── signup1/
├── signup/
├── static/
├── media/
├── assets/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .github/
```

---

## 📚 Documentation

- **Django:** https://docs.djangoproject.com/
- **Docker:** https://docs.docker.com/
- **GitHub Actions:** https://docs.github.com/en/actions

---

**Made with ❤️ using Django & Docker**
