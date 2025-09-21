# Django Server

A practice project to set up a **Django application** with a **local staging deployment pipeline** for learning and testing purposes.

---

## Project Overview

This project demonstrates:

- Setting up a basic Django app (`duck_app`)
- Creating a simple **GET API** for health check
- Running the server in **staging mode**
- Practicing CI/CD pipeline workflows for local deployment (GitHub Actions or custom script)

The goal is to simulate a real development workflow where code pushed to the `staging` branch triggers a pipeline that builds, tests, and deploys locally for validation.

---

## Installation & Setup

### Clone the repository

```
git clone git@github.com:tanveer-ahmad74/test_pipeline.git
cd test_pipeline
```

### Create a virtual Environment
```
python3 -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
```
### Running Migrations & Server
```
python manage.py migrate
python manage.py runserver 0.0.0.0:7000
```

Visit  http://0.0.0.0:7000/api/test/

You should see:
```
{
  "status": "success",
  "message": "Test API is working!",
  "environment": "staging"
}
```

### Run Test

```
pytest -v
```
