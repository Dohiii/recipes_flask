import sys
import time

from flask.cli import FlaskGroup
from src import create_app, db


'''
Here, is created a new FlaskGroup instance to 
extend the normal CLI with commands related to the Flask app.
'''

app = create_app()
cli = FlaskGroup(create_app=create_app)



'''
This registers a new command, recreate_db, to the CLI so that we can run it from the command line.

To run shell use command: docker-compose exec recipes flask shell

To apply the model to the database: docker-compose exec api python manage.py recreate_db

To run tests: docker-compose exec recipes python -m pytest -v "src/tests"
To run tests with coverage: docker-compose exec recipes python -m pytest "src/tests" -p no:warnings --cov="src"

To open postgress database: docker-compose exec recipes-db psql -U postgres

To check PEP8: docker-compose exec recipes flake8 src
To run Black check: docker-compose exec recipes black src --check
To run Black reformat: docker-compose exec recipes black src
To sort imports: docker-compose exec recipes isort src
'''



@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


# @cli.command('seed_db')
# def seed_db():
#     db.session.add(Book(title='Dune', authors=['Waldek kaczmarek'], published_year="2002"))
#     db.session.add(Book(title='Hobbit', authors=['R.R. Bings'], published_year="1976"))
#     db.session.commit()


if __name__ == '__main__':
    cli()

