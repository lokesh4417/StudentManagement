# Student Information Management System

A web-based Student Information Management System developed using Python Flask and SQLite. This project demonstrates student registration, login, information management, and student search functionality.

## Features

- Student registration
- Student login
- Student information management
- Update and delete student records
- Search students by name
- SQLite database integration
- Git and GitHub version control

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- Git
- GitHub

## Project Structure

StudentManagement/
├── app.py
├── database.py
├── registration.py
├── login.py
├── management.py
├── students.db
└── templates/

## Installation and Setup

1. Clone the repository:

   git clone https://github.com/lokesh4417/StudentManagement.git

2. Open the project directory:

   cd StudentManagement

3. Install Flask:

   python -m pip install flask

4. Run the application:

   python app.py

5. Open the application in your browser:

   http://127.0.0.1:5000

## Student Search API

Search for students by name using:

http://127.0.0.1:5000/search?name=Rahul

The API returns matching student records in JSON format.

## Version Control

This project uses Git branches, merging, commits, and GitHub for source-code management.

## Author

Lokesh