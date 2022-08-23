# FastAPI URL Shortener

## Install the Project

1. Create a Python virtual environment

```sh
$ python -m venv venv
$ source venv/bin/activate
(venv) $
```

2. Install the requirements

```
(venv) $ python -m pip install -r requirements.txt
```

## Run the Project

You can run the project with this command in your terminal:

```sh
(venv) $ uvicorn shortener_app.main:app --reload
```

Your server will reload automacially when you change a file.

## Verify Your Environment Variables

The project provides default environment settings in [`shortener_app/config.py`](shortener_app/config.py).
While you can use the default settings, [it's recommended](https://12factor.net/config) to create a `.env` file to store your settings outside of your production code. E.g.:

```config
# .env
ENV_NAME="Development"
BASE_URL="http://url.shortener"
DB_URL="sqlite:///./test_database.db"
```

With an `.env` file that contains the `ENV_NAME` variable with the value `"Development"` you can verify if your external `.env` file loads correctly:

```pycon
>>> from shortener_app.config import get_settings
>>> get_settings().env_name
... loading Settings
'Development'
```

To get an overview of the environment variables you can set, check the [`shortener_app/config.py`](shortener_app/config.py) file.

> ☝️ **Note:** You should never add the `.env` file to your version control system. 

## Visit the Documentation

When the project is running you can visit the documentation in your browser:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

## About the Author

Philipp Acsany - Email: philipp@realpython.com

## License

Distributed under the MIT license. See `LICENSE` in the root directory of this `materials` repo for more information.




    sudo apt-get update
    apt-get install python3-venv
    python3 -m venv venv
    source venv/bin/activate
    python -m pip install -r requirements.txt
    uvicorn shortener_app.main:app --reload

prod
uvicorn shortener_app.main:app --host="137.184.84.221"

137.184.84.221


 scp -r C:\Users\hp\Downloads\materials-fastapi-url-shortener\source_code_final root@137.184.84.221:/root


ps aux |grep uvicorn*



# FastAPI Fondeadora

#Instalación manual

    Ingresar al servidor vía ssh con public Key
    ssh root@137.184.84.221

    #Actualización
    sudo apt-get update

    #subir archivos del proyecto desde windows a server
    scp -r C:\Users\hp\short_app\short_app root@137.184.84.221:/root

    #Instalar venv
    apt-get install python3-venv
    python3 -m venv venv
    #Activar venv
    source venv/bin/activate
    #Instalar requerimientos
    python -m pip install -r requirements.txt
    #Activar app en local
    #uvicorn short_app.main:app --reload
    #Activar app en prod
    uvicorn short_app.main:app --host="137.184.84.221"

 
    #Buscar proceso uvicorn en linux
    ps aux |grep uvicorn*



