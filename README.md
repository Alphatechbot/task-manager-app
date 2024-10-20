Task-manager App Setup Guide

Prerequisites
Python (3.x recommended)
Django (installed via pip)

Getting Started
Clone the repository to your local machine:


git clone https://github.com/Alphatechbot/task-manager-app
Change to the project directory:


cd task-manager-app
Create a virtual environment (optional but recommended):


python -m venv venv
Activate the virtual environment:

On Windows:
venv\Scripts\activate

On macOS and Linux:
source venv/bin/activate
Install project dependencies:

pip install -r requirements.txt
Run migrations to set up the database:

Copy code
python manage.py migrate
Create a superuser account for the Django admin panel:
python manage.py createsuperuser
Start the development server:


python manage.py runserver
Your Django ToDo app should now be running locally at http://localhost:8000/.

Open a web browser and visit the admin panel at http://localhost:8000/admin/. 

Log in with the superuser credentials you created earlier.
