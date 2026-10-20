# Student Information Management System

## Overview

The Student Information Management System is a web-based application developed using Python Flask and SQLite to manage student information.

The application provides student registration, login, student record management, and student search functionality. It also demonstrates Git branching, merging, cloning, and GitHub-based version control as part of the development workflow.

---

# Features

## Student Registration
- Register student information through the application
- Store student details in an SQLite database

## Student Login
- Provides a student login module
- Integrates the login functionality with the Flask application

## Student Management
- View student records
- Update existing student information
- Delete student records

## Student Search
- Search student records by name
- Return matching student information in JSON format through a Flask endpoint

## Database Integration
- SQLite database integration
- Store and retrieve student records

## Version Control
- Git repository initialization
- Feature branches for separate modules
- Branch merging and conflict resolution
- GitHub repository integration
- Clone the project for further development

---

# Technology Stack

## Backend
- Python
- Flask

## Database
- SQLite

## Frontend
- HTML
- Jinja2 templates

## Development Tools
- Visual Studio Code
- Git
- GitHub

---

# Project Architecture

```text
                 User
                   |
                   v
             HTML Interface
                   |
                   v
              Flask App
                   |
          -------------------
          |         |       |
          v         v       v
     Registration  Login  Management
          |         |       |
          -------------------
                   |
                   v
              SQLite DB
                   |
                   v
             Student Records

          Flask Search Endpoint
                   |
                   v
             JSON Response
```

---

# Project Structure

```text
StudentManagement/
│
├── app.py
├── database.py
├── registration.py
├── login.py
├── management.py
├── students.db
├── templates/
│   ├── index.html
│   └── other HTML templates
├── .gitignore
└── README.md
```

The templates directory contains the HTML templates used by the application.

---

# Installation and Setup

## 1. Clone the Repository

```bash
git clone https://github.com/lokesh4417/StudentManagement.git
```

## 2. Open the Project Directory

```bash
cd StudentManagement
```

## 3. Create a Virtual Environment

```bash
python -m venv venv
```

## 4. Activate the Virtual Environment

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

## 5. Install Dependencies

```bash
python -m pip install Flask
```

## 6. Run the Application

```bash
python app.py
```

## 7. Open the Application

Open the following address in your browser:

http://127.0.0.1:5000

---

# Student Search API

The application provides a search endpoint to find student records by name.

## Endpoint

```text
GET /search?name=Rahul
```

## Local URL

```text
http://127.0.0.1:5000/search?name=Rahul
```

## Example JSON Response

```json
[
  {
    "id": 1,
    "name": "Rahul",
    "department": "CSE"
  }
]
```

The response above is an example. Actual results depend on the records in the database.

---

# Git and GitHub Workflow

The project demonstrates the following version-control operations:

- Creating a local Git repository
- Creating feature branches
- Committing individual modules
- Merging branches into the main branch
- Resolving merge conflicts
- Connecting the local repository to GitHub
- Pushing changes to a remote repository
- Cloning the repository for further development
- Updating the application and pushing new features

---

# Future Improvements

- Add more student search and filtering options
- Improve the user interface with responsive styling
- Add input validation and clearer error messages
- Improve authentication and access control
- Add pagination for large student lists
- Add automated testing
- Deploy the application to a hosting platform

---

# Developed By

**Lokesh Galiveti**

B.Tech Computer Science and Engineering  
Artificial Intelligence & Machine Learning

---

# License

This project was developed for educational purposes as part of learning Flask, SQLite, and Git/GitHub workflows.
