# DjangoAppTest

Practicing my Django web application skills here.

# How to run Program

### Install the virtualenv package
Install the virtualenv package to create and activate a virtual environment
```
pip install virtualenv
```

### Create virtual environment
```
virtualenv venv
```

### Activate the virtual environment

Mac OS / Linux
```
source venv/bin/activate
```

Windows
```
source venv/source/activate

--- or ---

venv\Scripts\activate
```

### Get necessary files to run the program in the virtual environment

pip has the option to install everything needed to run the program with requirements.txt
```
pip install -r requirements.txt
```


### Deactive the virtual environment
```
deactivate
```

### To run the server 

```
python manage.py runserver 8001
```

# Installs
1. django-multiselectfield

## django-multiselectfield
```
pip install django-multiselectfield
```

# Notes

### Requirements.txt

Make sure if there are any installs, plugins, or libraries added to add to the requirements.txt. This cab be done with the following command:
```
pip freeze > requirements.txt
```
