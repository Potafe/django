# Django Blog Application

This is a Django-based blogging platform that allows users to create, read, update, and delete blog posts. The project also includes a user authentication system and features like profile management and a responsive design.

---

# NOTE:
The site has been deployed using railway and koyeb, there are still some feature additions in progress such as sidebar completion, chat and comment section and also an integrated chatbot for the app. Meanwhile enjoy the app.

## 🚀 Features

- User authentication: Login, Signup, and Logout.
- Profile management with user-specific data.
- CRUD operations for blog posts.
- Responsive design using Bootstrap 4.
- Dynamic form rendering using `crispy_forms`.
- PostgreSQL database integration.
- Environment variable management with `.env`.

---

## 🛠️ Tech Stack

- **Backend**: Django 5.1.4
- **Frontend**: Bootstrap 4, HTML5, CSS3
- **Database**: PostgreSQL
- **Environment Management**: `python-dotenv`
- **Containerization**: Docker

---

## 🏗️ Installation and Setup

### Prerequisites

- Python 3.9+
- PostgreSQL installed and running
- Docker Desktop
- `pip` (Python package manager)

---

### Steps to Set Up Locally

1. **Clone the Repository**:
   ```bash
    git clone https://github.com/Potafe/django.git
    ```

2. **Go to the Repository**:
    ```bash
    cd django
    ```
3. **Create .env file similar to one given on .env.example**:
    ```js
    DEBUG=1
    DJANGO_SECRET_KEY=your_secret_key_here
    DB_NAME=postgres
    DB_USER=postgres
    DB_PASSWORD=postgres    
    DB_HOST=localhost
    DB_PORT=5432

    ```

4. **Running the app on locally on your system**:
    ```bash
    docker-compose up --build
    ```
5. **Visit the app on port localhost:8000**
