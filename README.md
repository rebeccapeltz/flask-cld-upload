# Flask Cloudinary Upload

## Setup Virtual Env

```bash
python3 -m venv env
source env/bin/activate
```

Deactivate virtual env

```bash
deactivate
source env/bin/activate
```

## Install Flask

```bash
python3 -m pip install Flask==1.1.1
```

## Add requirements.txt

python3 -m pip freeze > requirements.txt

## Run app locally

```bash
python3 app.py 
```
### upgrade pip

```bash
usr/local/opt/python@3.9/bin/python3.9 -m pip install --upgrade pip
python3 -m pip freeze > requirements.txt
```

## Heroku Deploy

```bash
touch Procfile
```

```bash
 python3 -m pip install gunicorn==20.0.4
 python3 -m pip freeze > requirements.txt
 ```

 Create `runtime.txt`

 ```bash
 python-3.8.1
 ```

 ```bash
git push heroku master
heroku open
git commit -m"...
heroku login
heroku create
heroku open
 ``` 

### Sample app
https://safe-tor-51739.herokuapp.com/ | https://git.heroku.com/safe-tor-51739.git

#### Summary of heroku deploy

1. `virtualenv env`
1. `pip3 install flask`
1. `pip3 install gunicorn`
1. `git init`
1. add .gitignore with `env` and `.env`
1. add Procfile with `web: gunicorn --worker-class eventlet -w 1  application:app`
1. run `pip3 freeze > requirements.txt`
1. `git commit -m"...`
1. `heroku login`
1. `heroku create`
1. set up cloudinary env variables in heroku
1. `git push heroku master`
1. `heroku open`

## Env variables
Save .env.sample as .env (it will be gitnignored). Then add your own Cloudinary credentials that you get from the Console.

```bash
touch .env
python3 -m pip install python-dotenv
python3 -m pip freeze > requirements.txt
```

```python
from dotenv import load_dotenv
load_dotenv()
cloudinary.config(cloud_name = os.getenv('CLOUD_NAME'), api_key=os.getenv('API_KEY'), 
    api_secret=os.getenv('API_SECRET'))
```

## Cloudinary

```bash
 python3 -m pip install cloudinary
 python3 -m pip freeze > requirements.txt
 ````

 See app.js code for sample upload import and command.