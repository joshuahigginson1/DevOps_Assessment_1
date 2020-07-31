"""
Dev Notes: So our application factory returns our Flask app within the variable 'app'.
However, where do we return app to, exactly? That's where the mysterious wsgi.py file comes into play.

WSGI is the Web Server Gateway Interface. WSGI is a Python standard described in detail in PEP 3333.

It is a specification that describes how a web server communicates with web applications.
It is how web applications can be chained together to process one request.

WSGI.py is a file in our app's root directory that can serve as our 'entry point'.

When setting up a production web server to point to your app, we will almost always configure it to point to wsgi.py.
This in turn imports, and starts our entire app.
"""

# Imports --------------------------------------------------------------------------------

from flaskr import create_app  # imports our app object from ./flask-app/flaskr/__init__.py

# Define Variables -----------------------------------------------------------------------

app = create_app()

# Execute Code ---------------------------------------------------------------------------


if __name__ == "__main__":
    app.run(host='0.0.0.0')
