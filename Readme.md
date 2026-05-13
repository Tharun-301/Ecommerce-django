# 🛒 VibeKart — Full Stack Django Ecommerce Platform

## Live Demo

* Live Website: [http://django-vibekart-env.eba-trwhfnr8.us-west-2.elasticbeanstalk.com/](http://django-vibekart-env.eba-trwhfnr8.us-west-2.elasticbeanstalk.com/)

---

# 🚀 Overview

VibeKart is a production-style ecommerce web application built with Django, PostgreSQL, AWS Elastic Beanstalk, and AWS S3.

This project focuses on real-world backend architecture, authentication systems, product management, cart functionality, review systems, media handling, cloud deployment, and scalable production configuration.

✅ Production-style Django architecture
✅ Cloud deployment using AWS Elastic Beanstalk
✅ PostgreSQL + AWS RDS integration
✅ AWS S3 media & static storage
✅ Ecommerce cart & variation workflow
✅ Review & rating system
✅ Scalable deployment configuration

Unlike tutorial-level CRUD projects, this application includes deployment-grade infrastructure and production-oriented implementation.

---

# 🛠️ Tech Stack

## Backend

* Python
* Django
* Django REST Framework
* Gunicorn

## Database

* PostgreSQL (AWS RDS)

## Frontend

* HTML5
* CSS3
* Bootstrap
* JavaScript

## Cloud & Deployment

* AWS Elastic Beanstalk
* AWS EC2
* AWS S3
* Nginx
* Gunicorn

## Version Control

* Git
* GitHub

---

# ✨ Core Features

## Authentication System

* User Registration
* Login / Logout
* Password Validation
* Session Handling
* User Dashboard
* Protected Routes

## Ecommerce Features

* PayPal Payment Gateway Integration
* Secure Online Payments
* Order Checkout Workflow
* Product Listing
* Product Categories
* Product Variations (Color & Size)
* Product Gallery
* Dynamic Product Detail Page
* Add to Cart
* Quantity Management
* Cart Persistence
* Checkout Flow

## Product Review System

* Product Ratings
* Star-Based Reviews
* Review Aggregation
* Average Rating Calculation
* Review Count System

## Admin Features

* Product Management
* Category Management
* Variation Management
* Review Moderation
* Inventory Management

## Cloud Storage

* Static Files Stored in AWS S3
* Media Files Stored in AWS S3
* Optimized Production Media Delivery

---

# ☁️ Production Deployment Highlights

## Elastic Beanstalk Deployment

Configured and deployed a production-ready Django application using:

* Elastic Beanstalk
* Gunicorn
* Nginx
* Procfile Configuration
* Environment Variables
* Production Settings

## AWS S3 Integration

Implemented cloud-based storage for:

* Product Images
* Static Assets
* Media Uploads

## PostgreSQL Integration

Migrated application from SQLite to PostgreSQL using AWS RDS for production-grade database management.

---

# 🧠 System Architecture

```text
Client Browser
      ↓
Elastic Beanstalk
      ↓
Nginx
      ↓
Gunicorn
      ↓
Django Application
      ↓
PostgreSQL (RDS)
      ↓
AWS S3 (Media & Static Files)
```

---

# 🔥 Key Engineering Challenges Solved

## Production Deployment Issues

* Fixed Gunicorn startup configuration
* Solved Procfile deployment errors
* Configured Nginx correctly for Django
* Resolved AWS IAM permission issues

## Static & Media Handling

* Migrated local media to AWS S3
* Configured django-storages
* Solved broken media paths in production
* Optimized static asset delivery

## Database Migration

* Migrated from SQLite to PostgreSQL
* Handled production migrations safely
* Connected Django with AWS RDS

## Git & Repository Cleanup

* Cleaned deployment artifacts from Git history
* Prevented large deployment ZIP uploads
* Configured proper .gitignore structure

---

# 📁 Project Structure

```text
VibeKart/
│
├── accounts/
├── carts/
├── category/
├── orders/
├── store/
├── templates/
├── static/
├── media/
├── vibekart_main/
├── requirements.txt
├── Procfile
├── manage.py
└── .ebignore
```

---

# ⚙️ Installation & Setup

## Clone Repository

```bash
git clone https://github.com/Tharun-301/Ecommerce-django.git
cd Ecommerce-django
```

## Create Virtual Environment

```bash
python -m venv env
```

## Activate Environment

### Windows

```bash
env\Scripts\activate
```

### Linux / Mac

```bash
source env/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Migrations

```bash
python manage.py migrate
```

## Create Superuser

```bash
python manage.py createsuperuser
```

## Run Server

```bash
python manage.py runserver
```

---

# 🔐 Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=5432
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_STORAGE_BUCKET_NAME=your_bucket_name
AWS_S3_REGION_NAME=your_region
```

---

# ☁️ AWS Services Used

| Service               | Purpose                      |
| --------------------- | ---------------------------- |
| AWS Elastic Beanstalk | Application Hosting          |
| AWS EC2               | Compute Infrastructure       |
| AWS S3                | Static & Media Storage       |
| AWS RDS               | PostgreSQL Database          |
| IAM                   | Access Control & Permissions |

---

# 💡 Skills Demonstrated

* Full Stack Django Development
* Cloud Deployment
* AWS Infrastructure
* PostgreSQL Integration
* Authentication Systems
* Media & Static File Management
* Production Debugging
* Git Version Control
* Backend Architecture
* Ecommerce Workflow Design
* REST API Fundamentals
* Server Configuration

---

# 💳 Payment Integration

## PayPal Integration

* Secure PayPal Checkout
* Payment Success & Failure Handling
* Transaction Workflow Management
* Future Stripe Integration Support

---

# 📈 Future Improvements

* Payment Gateway Integration
* Order Tracking System
* Wishlist Functionality
* Docker Deployment
* CI/CD Pipeline
* Redis Caching
* Elasticsearch Integration
* JWT Authentication
* Recommendation Engine
* Advanced Analytics Dashboard

---

# 🎯 Why This Project Matters

This project demonstrates the ability to:

* Build production-grade Django applications
* Deploy scalable backend systems
* Configure AWS cloud infrastructure
* Debug real deployment problems
* Manage databases and cloud storage
* Implement practical ecommerce workflows

The focus was not just building features, but understanding how modern backend systems operate in production environments.

---

# 👨‍💻 Author

## Tharun

Backend Developer | Django Developer | Python Developer

GitHub: https://github.com/Tharun-301

---

# 📜 License

This project is developed for learning, portfolio, and demonstration purposes.
