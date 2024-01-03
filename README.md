# Sofware for Household expenses (SOFHE)

Backend part of the SOFHE project.

## Tools used:

- Django
- Django-rest-framework
- MYSQL
- CELERY

To run the project:

## 1. Create and active virutal environment

Open the terminal and enter the following cmd.

```
virutalenv venv
venv\Scripts\Activate
```

## 2. Install all the dependencies

After activating virutal environment, install the requirements.

```
pip install -r require.txt
```

## 3. Open Terminal and go to project directory and run the project

After all the libraries are set, let's run the project.
Go to the directories where manage.py is allocated.

```
cd sofhe/

python manage.py runserver
```

## 4. Go to web browser and enter following url to view all the available url using SWAGGER-API.

To see the endpoints and schema used go to the following links.

```
127.0.0.1:8000/schema/docs/
```

You can see the different api. To test, click on the api and press try it out.
