Create a virtual environment:
	python -m venv .\.virtualenvs\escola
Activate venv:
	.\.virtualenvs\minha_virtualenv\Scripts\activate
Install psycopg2 module:
	pip install psycopg2
Select the venv as your interpreter.

On PostgreSQL:
	Create Database escola
Execute 'BDEscola.sql' script to create the tables.


Create a 'database.ini' file in the folder with your information:
	[postgresql]
	host=localhost
	database=escola
	user=[your_user]
	password=[your_password]