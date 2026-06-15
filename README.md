# 📝Feedback Board

A simple feedback management system built with FastAPI, SQLite, SQLAlchemy, and Bootstrap.

---

## 📌 Overview

This project allows users to submit feedback and enables administrators to review and update the status of submitted feedback through a dashboard.

The application was developed as a small end-to-end product, focusing on simplicity, maintainability, and rapid delivery.

---

## 👩🏻‍💻 Developer

**Seyyedeh Fargol Nazemzadeh**

---

## ✨ Features

### 👤 User Side

* Submit feedback
* Provide a title and message
* Automatic feedback status assignment

### 🛡️ Admin Dashboard

* View all submitted feedback
* Track feedback status
* Update feedback status

### 📬 Supported Statuses

* Registered
* Under Review
* Resolved

---

## ⚙️ Technology Stack

### 🌐 Backend

* FastAPI
* SQLAlchemy
* SQLite

### 🎨 Frontend

* Jinja2 Templates
* Bootstrap 5

---

## 💡 Technical Decisions

### Why FastAPI?

FastAPI provides a lightweight and modern framework that allows rapid backend development while keeping the codebase clean and maintainable.

### Why SQLite?

SQLite is sufficient for the scope of this project and requires zero external configuration, making the setup process simple.

### Why Server-Side Rendering?

Since the project requirements are relatively small, Jinja2 templates provide a simpler solution than introducing a separate frontend framework.

---

## 🗂️ Project Structure

```text
feedback-board/
│
├── app/
│   ├── crude.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│   │
│   ├── templates/
│   │   ├── dashboard.html
│   │   └── feedback.html
│   │
│   └── static/
│       └── css/
│           └── style.css
│
├── screenshots/
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation

### Clone Repository

```bash
git clone https://github.com/Fargolnz/Feedback-Board.git
cd Feedback-Board
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
uvicorn app.main:app --reload
```

### Open

```text
http://127.0.0.1:8000
```

---

## 🖼️ Screenshots

### 💬 Feedback Submission Page

![Feedback](screenshots/feedback-screenshot.png)

### 💻Dashboard

![Dashboard](screenshots/dashboard-screenshot.png)