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

## Heroku Deploy

```bash
touch Procfile

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

https://safe-tor-51739.herokuapp.com/ | https://git.heroku.com/safe-tor-51739.git

git push heroku master
heroku open

usr/local/opt/python@3.9/bin/python3.9 -m pip install --upgrade pip
python3 -m pip freeze > requirements.txt