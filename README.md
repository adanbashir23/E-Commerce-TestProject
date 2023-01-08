# EcommerceApp-TestProject
This Test Project was created by me during my training in DevSinc. It was implemented using Django.

# Prerequisites
* Things to consider:
        Configurations of tools used.
# EcommerceApp-TestProject
Python Version:
* Version : 3.8.10

System Dependencies
* Django 4.1
* Postgresql 14

Packages
* jquery
* cloudinary
* bootstrap
* font-awesome
* isort

Configurations:
1. Clone the code from github before starting.
2. Make sure to install the system dependencies before starting of above mentioned versions.

Steps to follow:
1. Install venv.
2. Install python and django dependencies.
  Use the following commands to install the dependencies:
    pip install -r requirements.txt
3. Install Postgresql and set up a user profile. Add the user credentials.
4. Cloudinary credentials must also be set in the credentials.
5. Set up the database by using rails db:setup.
6. Install all the packages required using the command: pip install

Deployment instructions:
1. Enable automatic deployment on Heroku for easy deployment after pushing all your finalised code on github.

To test models:
1. Run python3 manage.py shell in console, to test the models and associations.

To start the Django server:
1. python3 manage.py runserver.

* Django Server: http://localhost:8000/

* Application live at https://e-commerce-testproject.herokuapp.com/
