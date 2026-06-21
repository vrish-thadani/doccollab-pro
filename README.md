DocCollab Pro

Cloud-Based Collaborative Document Management System built using Flask, SQLite, HTML, CSS, and JavaScript.

GitHub Repository

Repository Link:
https://github.com/vrish-thadani/doccollab-pro

⸻

Project Overview

DocCollab Pro is a collaborative document management platform that enables multiple users to create, edit, review, and manage documents through a centralized workspace.

The system includes document editing, version control, comment management, team collaboration, analytics monitoring, and conflict resolution functionalities. The project demonstrates the core concepts behind modern collaborative platforms such as Google Docs and Microsoft Office Online.

⸻

Problem Statement

Managing documents through traditional file sharing methods often results in duplicate copies, version conflicts, inconsistent data, and poor collaboration among team members.

The objective of this project is to provide a centralized platform that allows users to collaborate efficiently while maintaining document history, version tracking, and communication records.

⸻

Proposed Solution

DocCollab Pro provides:

* Collaborative document editing
* Document version control
* Team management
* Comment management
* Analytics dashboard
* Conflict resolution
* Centralized document storage

The platform helps users work together while ensuring document consistency and version integrity.

⸻

Features

* Collaborative document editor
* Version history management
* Team management module
* Comment management system
* Analytics dashboard
* Conflict resolution module
* SQLite database integration
* Flask-based backend architecture

⸻

System Architecture

The project follows a Three-Layer Architecture:

Presentation Layer

* HTML
* CSS
* JavaScript
* Web Browser Interface

Application Layer

* Flask Application Server
* Document Editor Module
* Version Control Module
* Comment Management Module
* Team Management Module
* Analytics Module
* Conflict Resolution Module

Data Layer

* SQLite Database
* Documents Table
* Comments Table
* Versions Table
* Users Table

⸻

Technology Stack

Frontend

* HTML5
* CSS3
* JavaScript

Backend

* Python Flask

Database

* SQLite

Development Tools

* Visual Studio Code
* GitHub
* Draw.io

⸻

Project Structure

doccollab-pro/
│
├── app.py
├── requirements.txt
├── README.md
│
├── database/
│   └── doccollab.db
│
├── static/
│   ├── app.js
│   ├── style.css
│   ├── dashboard.css
│   ├── editor.css
│   └── login.css
│
└── templates/
    ├── login.html
    ├── dashboard.html
    ├── editor.html
    ├── comments.html
    ├── versions.html
    ├── team.html
    ├── analytics.html
    ├── conflicts.html
    └── architecture.html

⸻

Dependencies

Install the following dependency:

Flask==3.0.3

⸻

Setup Instructions

Step 1: Clone Repository

git clone https://github.com/vrish-thadani/doccollab-pro.git

Step 2: Navigate to Project Directory

cd doccollab-pro

Step 3: Install Dependencies

pip install -r requirements.txt

⸻

Execution Steps

Run the Flask application:

python app.py

After successful execution, open:

http://127.0.0.1:5000

in your web browser.

⸻

Modules Implemented

Dashboard Module

Provides project statistics and collaboration overview.

Document Editor Module

Allows users to edit and manage documents.

Version Control Module

Tracks document versions and history.

Comment Management Module

Supports collaboration through comments.

Team Management Module

Displays project members and roles.

Analytics Module

Provides project insights and metrics.

Conflict Resolution Module

Handles simultaneous editing conflicts.

⸻

Future Scope

* Real-time collaboration using WebSockets
* Cloud deployment on AWS or Azure
* Mobile application support
* AI-assisted document editing
* Advanced conflict resolution techniques
* User authentication and authorization
* File upload support
* Notification system integration

⸻

Conclusion

DocCollab Pro successfully demonstrates a cloud-based collaborative document management system using Flask and SQLite. The project integrates document editing, version tracking, collaboration tools, analytics, and conflict resolution into a single platform, providing an effective solution for collaborative document management.
