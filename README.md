<h1 style="text-align: center;">ProMan</h1>

***
**ProMan is a Flask based project management tool where the user can make boards for their projects and assign task cards to them, according in which status the task is. If one task is finished they can drag it and drop it to the current status column. Users can also register, log in and log out from the application.**
***
## Requirements

* Python
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
##### step into the project folder
```
cd proman-2-python-RRicsi89
```
##### fill the .env file with the corresponding data (the HOST most probably will be localhost)
```
MY_PSQL_DBNAME=
MY_PSQL_USER=
MY_PSQL_PASSWORD=
MY_PSQL_HOST=
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
##### quit from postgres shell and step back to the project root folder:
```
$ \q
$ cd ..
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

##### if the requirements.txt install fails building wheel for psycopg2 this should fix it:
```
$ sudo apt-get install libpq-dev
(venv) $ pip install -r requirements.txt
```

Note for Microsoft Windows users: replace the virtual environment activation command above with venv\Scripts\activate.

#### Run the program: 
```
python main.py
```
