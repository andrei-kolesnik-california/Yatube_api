# 🚀 Yatube API — Social Media Platform API

[![Python](https://img.shields.io/badge/Python-3.8.3-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-2.2.16-green.svg)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/Django%20REST%20Framework-3.12.4-red.svg)](https://www.django-rest-framework.org/)

> A powerful REST API for a social media platform where users can share posts, interact through comments, join groups, and follow other authors.

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Quick Start](#-quick-start)
- [API Documentation](#-api-documentation)
- [Contributing](#-contributing)

## 🎯 Overview

Yatube API is a comprehensive social media platform backend built with Django REST Framework. It provides a robust foundation for creating, managing, and interacting with social media content. The platform supports user authentication via JWT tokens and offers both public (read-only) and authenticated user experiences.

### Key Features:
- **User Authentication**: Secure JWT-based authentication system
- **Content Management**: Create, read, update, and delete posts
- **Social Interactions**: Comments, follows, and group memberships
- **Database**: SQLite for data persistence and management
- **RESTful API**: Clean, intuitive API endpoints

## ✨ Features

### 🔐 Authentication & Authorization
- JWT token-based authentication
- Secure user registration and login
- Role-based access control

### 📝 Content Management
- Create and manage posts
- Add comments to posts
- Edit and delete user content
- Media support for rich content

### 👥 Social Features
- Follow/unfollow other users
- Join and participate in groups
- User profiles and activity feeds

### 📊 Data Management
- SQLite database for reliable data storage
- Efficient data retrieval and caching
- Comprehensive data validation

## 🛠 Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.8.3 | Core programming language |
| **Django** | 2.2.16 | Web framework |
| **Django REST Framework** | 3.12.4 | API development |
| **Djoser** | 2.1.0 | Authentication endpoints |

📦 **Complete dependency list**: See [`requirements.txt`](requirements.txt)

## 🚀 Quick Start

### Prerequisites
- Python 3.8.3 or higher
- Git
- Virtual environment tool

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone git@github.com:andrei-kolesnik-california/Yatube_API.git
   cd Yatube_API
   ```

2. **Create and activate virtual environment**
   
   **For Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   
   **For macOS/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python3 manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python3 manage.py runserver
   ```

6. **Access the application**
   - API Root: http://localhost:8000/
   - Admin Panel: http://localhost:8000/admin/
   - API Documentation: http://localhost:8000/redoc/

## 📚 API Documentation

Once the server is running, you can access the comprehensive API documentation at:

**🔗 [http://localhost:8000/redoc/](http://localhost:8000/redoc/)**

The documentation includes:
- All available endpoints
- Request/response examples
- Authentication methods
- Data models and schemas

## 🤝 Contributing

We welcome contributions! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- Built with Django REST Framework
- Authentication powered by Djoser
- Documentation generated with ReDoc

---

<div align="center">
  <p>Made with ❤️ for the developer community</p>
  <p><a href="#-yatube-api--social-media-platform-api">⬆️ Back to top</a></p>
</div>