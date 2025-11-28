# Secure-Authentication-System-Flask-Backend-API

A production-ready secure authentication system built with Flask, featuring user registration, encrypted password storage, session-based authentication, and protected routes. This project follows backend security best practices and is designed to be CV- and interview-ready.
It demonstrates real-world backend development skills including form validation, password hashing, session management, and database security using SQLite and Flask-Bcrypt.

Key Features:
  Secure user registration & login system
  Hashed passwords using industry-standard encryption
  Session-based authentication
  Protected dashboard route
  Logout functionality
  Duplicate email prevention at database level
  SQL Injection protection using parameterized queries
  Flash messaging for user feedback
  Clean and scalable backend structure
  Production-safe configuration (no debug mode, secure secret key handling)

🛠️ Tech Stack:
  Backend Framework: Flask (Python)
  Database: SQLite
  Security: Flask-Bcrypt, WTForms Validation
  Authentication: Session-based login system
  Frontend Integration: Jinja2 Templates (HTML)

Project Structure:
  /Secure-Authentication-System
  │── main.py
  │── Database.db
  │── templates/
  │   ├── login.html
  │   ├── Sign.html
  │   └── Dashboard.html

🚀 How to Run the Project Locally:
  # 1. Install dependencies
  pip install flask flask-wtf flask-bcrypt email-validator
  
  # 2. Run the application
  python main.py

  Then open your browser and go to:
    http://127.0.0.1:5000

🔒 Security Highlights:
  Passwords are never stored in plain text
  Email uniqueness enforced directly in the database
  All database queries use safe placeholders
  User sessions protect private routes
  No sensitive data exposed through routes


🎯 Purpose of This Project:
  This project was built to:
    Demonstrate real-world backend authentication
    Practice secure user management
    Serve as a portfolio project for junior backend roles
    Showcase understanding of production-level security concepts

📈 Future Improvements
  🔐 JWT Authentication (API mode)
  👤 Admin & User role system
  🔁 Password reset via email
  ✅ Email verification
  🌐 Deployment to a live server
