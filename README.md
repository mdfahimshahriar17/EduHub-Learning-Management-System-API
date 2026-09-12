# EduHub — Learning Management System

EduHub is a Learning Management System (LMS) currently being developed using Django and Django REST Framework. The project focuses on building a scalable backend API with authentication, authorization, course management, lesson management, quizzes, and supporting learning materials. The backend is currently under development, and a React.js frontend will be integrated in the next phase.

## Project Status

**Status: Under Development**

## Current Features

- Custom User Model
- User Registration
- JWT Authentication
- Access Token & Refresh Token
- Refresh Token Rotation
- Refresh Token Blacklisting
- Login & Logout
- Password Reset Flow
- User Roles: Student, Instructor, Admin
- Role-Based Permissions
- Course Creation
- Course Listing
- Lesson Creation
- Lesson Listing
- Lesson Ordering
- Lesson Video Upload
- Supporting Document Upload
- Quiz System
- PostgreSQL Database

## Technologies Used

### Backend
- Python
- Django
- Django REST Framework
- Simple JWT
- PostgreSQL

### Frontend
- React.js (Planned)

### Tools
- Git
- GitHub
- VS Code

## User Roles

EduHub currently supports three main user roles:

- **Student** — Can access available learning content.
- **Instructor** — Can create and manage courses and learning content.
- **Admin** — Responsible for administrative management.

Role-based permissions are implemented to control access to different API operations.

## Authentication

EduHub uses JWT (JSON Web Token) authentication through Django REST Framework Simple JWT.

The authentication system currently includes:

- User Registration
- JWT Login
- Access Tokens
- Refresh Tokens
- Refresh Token Rotation
- Refresh Token Blacklisting
- Logout
- Password Reset Flow

## Course Management

The course system allows instructors to create and manage learning content.

Current course-related functionality includes:

- Course Creation
- Course Listing
- Lesson Creation
- Lesson Listing
- Lesson Ordering
- Lesson Video Upload
- Supporting Document Upload
- Quiz System
- Instructor-based Course Permissions

The system is designed so that instructors can manage their own courses while students can access available learning content.

## Database

EduHub uses PostgreSQL as its primary database.

The current database structure includes relationships between users, courses, lessons, supporting documents, and quizzes.

    User
     │
     └── Course
          │
          └── Lesson
               ├── Supporting Documents
               └── Quizzes

## Project Structure

    EduHub-Learning-Management-System-API/
    │
    ├── accounts/
    │   ├── models.py
    │   ├── serializers.py
    │   ├── views.py
    │   └── admin.py
    │
    ├── course/
    │   ├── models.py
    │   ├── serializers.py
    │   ├── permissions.py
    │   └── views.py
    │
    ├── EduHub_Learning_Management_API/
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    │
    ├── manage.py
    ├── requirements.txt
    └── README.md


## Future Development

EduHub is planned to evolve into a complete Learning Management System with a Django REST Framework backend and a modern React.js frontend.

Planned features include:

- React.js Frontend
- Complete Course CRUD
- Complete Lesson CRUD
- Student Enrollment
- Quiz Submission and Evaluation
- Student Course Progress Tracking
- Instructor Dashboard
- Student Dashboard
- User Profile Management
- Course Ratings and Reviews
- Advanced File and Video Management
- Email-based Password Reset
- API Documentation
- Automated Testing
- Docker Support
- Production Deployment
- API Performance and Query Optimization

## Project Goal

The goal of EduHub is to develop a professional and scalable Learning Management System while applying real-world software development practices.

The project is being developed incrementally with a strong focus on Django REST Framework, JWT authentication, role-based authorization, relational database design, API development, and eventually a modern React.js frontend.

## Note

EduHub is currently under active development. The API structure, features, and project architecture may change as new functionality is implemented.