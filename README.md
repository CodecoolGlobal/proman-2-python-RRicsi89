<h1 style="text-align: center;">ProMan</h1>

***
**ProMan is a Flask based project management tool where the user can make boards for their projects and assign task cards to them, according in which status the task is. If one task is finished they can drag it and drop it to the current status column. Users can also register, log in and log out from the application.**
***
## Requirements

* Python
* If your Python version lower than 3.3 (check with `python --version`), you'll need to install the venv module (`pipx install virtualenv`)
* git (only to clone this repository)
* PostgreSQL

***

## Installation / How to start
##### clone the project:
```
git clone https://github.com/CodecoolGlobal/proman-2-python-RRicsi89.git
```
##### create a local PostgreSQL database for this project to use e.g. :
```
createdb proman
```
##### create a .env file
```
touch .env
```
##### copy the .env.template file's content to the newly created .env file and fill it with the corresponding data (the HOST most probably will be localhost)
```
MY_PSQL_DBNAME=
MY_PSQL_USER=
MY_PSQL_HOST=
MY_PSQL_PASSWORD=
```
##### start psql in a terminal at the data folder of the project:
```
$ cd data
$ psql
```

##### connect to the new database, e.g.:
```
\connect proman
```
##### execute the commands in the SQL file:
```
\i proman_sample_data.sql
```
##### quit from postgres shell:
```
\q
```
##### create virtual environment:
```
virtualenv venv
```
##### start the virtual environment:
```
. venv/bin/activate
```
##### install the requirements to the virtual environment
```
(venv) pip install -r requirements.txt
```

Note for Python 3.4 users: replace virtualenv with pyvenv.
Note for Microsoft Windows users: replace the virtual environment activation command above with venv\Scripts\activate.

#### Run the program: 
```
python main.py
```
