🎓 School Institute – Django Project

This is a Django-based web application for managing Teachers and Students.
It demonstrates how to build and structure a Django project with multiple apps, templates, models, and admin support.

  

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-green?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)
[![Issues](https://img.shields.io/github/issues/franklinosuji2-afk/School_institute)](https://github.com/franklinosuji2-afk/School_institute/issues)
[![Stars](https://img.shields.io/github/stars/franklinosuji2-afk/School_institute?style=social)](https://github.com/franklinosuji2-afk/School_institute)



📂 Project Structure  

project2/
│── manage.py # Django project management script
│── README.md # Project documentation
│── db.sqlite3 # Local SQLite database (development)
│── .gitignore
│
├── school_institute/ # Main Django project
│ ├── settings.py # Project settings
│ ├── urls.py # Root URL routing
│ ├── views.py # Project-level views
│ ├── wsgi.py / asgi.py # Deployment entry points
│
├── students/ # Students app
│ ├── models.py # Student models
│ ├── views.py # Student views
│ ├── urls.py # Student URLs
│ ├── templates/students/ # Student templates
│ └── admin.py # Student admin config
│
├── teachers/ # Teachers app
│ ├── models.py # Teacher models
│ ├── views.py # Teacher views
│ ├── urls.py # Teacher URLs
│ ├── templates/teachers/ # Teacher templates
│ └── admin.py # Teacher admin config
│
└── templates/ # Shared templates
├── welcome.html
├── bye.html
└── school_institute/


✨ Features  

- ✅ Separate apps for **Teachers** and **Students**  
- ✅ Add, update and view teachers and students  
- ✅ Fully functional **Django Admin Panel**  
- ✅ Templates for student/teacher details and listings  
- ✅ Lightweight **SQLite** database for development  



🛠️ Setup & Installation (Powershell) 

1. *Clone the repository*


git clone https://github.com/franklinosuji2-afk/School_institute.git
cd School_institute
Create and activate a virtual environment



# Windows
python -m venv venv
venv\Scripts\activate

Linux
python3 -m venv venv
Install dependencies



pip install django
Apply migrations



python manage.py makemigrations
python manage.py migrate
Create an admin user



python manage.py createsuperuser
Run the development server



python manage.py runserver
🌐 Access the Application
Home: http://127.0.0.1:8000/

Students: http://127.0.0.1:8000/students/

Teachers: http://127.0.0.1:8000/teachers/

Admin Panel: http://127.0.0.1:8000/admin/

📌 .gitignore
The project ignores files that shouldn’t be tracked in Git, such as:

__pycache__/, *.pyc → Python cache files

db.sqlite3 → Local development database

venv/ → Virtual environment

.vscode/, .idea/ → Editor settings

🚀 Contributing & Git Workflow
When you make changes:



git pull origin main        # pull latest changes first
git add .                   # stage changes
git commit -m "Describe your changes"
git push origin main        # push to GitHub


👤 Author
     Franklin Osuji

💼 GitHub:
   franklinosuji2-afk

📧 Email: 
   franklin.osuji2@gmail.com

- LinkedIn:
  https://www.linkedin.com/in/franklin-osuji-a96003321/📝 License

📝License
This project is for educational/demo purposes.
Feel free to fork and adapt it for your own Django learning.
