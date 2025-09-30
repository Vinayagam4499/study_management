# study_management
A simple Django web application to perform CRUD (Create, Read, Update, Delete) operations for "Study" records using MySQL.

Features

Add new studies with fields: Name, Description, Phase, Sponsor Name

View study details

Edit existing studies

Delete studies

Sponsor Name shows previously entered values (datalist)

Logging and exception handling

Tech Stack

Python 3.x

Django 4.x

MySQL

HTML / CSS (templates)


CREATE DATABASE studydb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'studyuser'@'localhost' IDENTIFIED BY 'yourpassword';
GRANT ALL PRIVILEGES ON studydb.* TO 'studyuser'@'localhost';
FLUSH PRIVILEGES;


DJANGO_SECRET_KEY=your-secret-key
MYSQL_DB=studydb
MYSQL_USER=studyuser
MYSQL_PASSWORD=yourpassword
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306



python manage.py makemigrations
python manage.py migrate

python manage.py runserver


Usage

Home page: Shows list of studies

Add Study: Click 'Add Study' and fill the form

View: Click 'View' link to see details

Edit: Click 'Edit' link to update

Delete: Click 'Delete' button to remove study
