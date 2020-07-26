"""
Task: The __init__.py serves double duty. It will contain the application factory.
It also tells Python that the 'flaskr' directory should be treated as a package.



Dev Notes:


"""

# Imports --------------------------------------------------------------------------------

# import Flask class from the flask module
from flask import Flask

# create a new instance of Flask, and store it in variable app
app = Flask(__name__)

# import the ./application/routes.py file
from application import routes

# Define Variables -----------------------------------------------------------------------