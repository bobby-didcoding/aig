# Tech exercise for AIG
***
***

## Prerequisites
- Python=>3.10

***
***

## Getting started
First you will need to clone down the first module.

1) Create a new directory on your local machine. I have called mine agi. This is your 'root directory'.

2) Open a terminal and cd into the root directory.

3) You can now clone the main branch. You can do this a few different ways. I use SSH...

```
#option 1 - SSH
git clone --branch main git@github.com:bobby-didcoding/agi.git .

#option 2 - Github CLI
gh repo clone bobby-didcoding/agi .
git checkout main

#option 3 - HTTPS
git clone --branch main https://github.com/bobby-didcoding/agi.git .
```

***
***

## Environment variables
Create a new .env file for the project and add your won information as required
```
# windows machine
copy env.template .env

#mac/linux
cp env.template .env
```

***
***

## Create a new virtual env & install project requirements

```
python -m venv venv
venv\Scripts\activate.bat
pip install -r backend/requirements.txt
```

***
***

## Migrate the tables and run server

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

***
***

## Lastly, create a mediafiles dir

The easiest way to do this is to simply copy the media dir and name it 'mediafiles'.
