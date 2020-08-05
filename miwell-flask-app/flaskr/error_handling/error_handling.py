# This script handles errors and error remarks for our application.

# Imports --------------------------------------------------------------------------------

from flask import render_template, Blueprint, current_app, abort, request

from time import sleep

import os  # For walking the file system, in particular in our generate_error_photo function.

import random  # For randomly selecting error photos and error remarks.

# Blueprint Configuration -----------------------------------------------------------------


error_handling_bp = Blueprint(
    'error_handling_bp',  # Name we want to assign to our Blueprint for Flask's internal routing purposes.
    __name__,
    template_folder='templates',
    static_folder='static'
)


# Functions --------------------------------------------------------------------------------


def generate_error_remark():
    # generate a new file object from error_remarks.txt & call it's  __enter__ function.

    with open('miwell-flask-app/flaskr/static/error_handling/error_remarks.txt', 'r') as error_remarks:
        remark_list = error_remarks.readlines()  # Put each line of error_remarks.txt into a list array.
        random_remark = random.choice(remark_list)

    # Here, we break the context and call it’s __exit__ functionality, defaulting to self.close().

    return random_remark


def generate_error_photo():
    photo_path_list = []  # Initialise new photo path list.
    photo_file_list = []  # Initialise new photo file list.

    # Walk the project file system, and get the names of every photo in our error_handling/error_photos static folder.

    for root, dirs, files in os.walk("miwell-flask-app/flaskr/static/error_handling/error_photos"):
        for file in files:  # files returns as a list. Go through every file within our files.
            if file.endswith('.jpeg'):  # If file is a jpeg file...
                photo_file_path = os.path.join(root, file)  # Creates the relative file path to a photo.
                photo_path_list.append(photo_file_path)  # Append the photo file path to our photo_path_list list.
                photo_file_list.append(file)

    random_photo_path = random.choice(photo_path_list)  # Pick a random photo from it's relative link.
    random_photo_name = random.choice(photo_file_list)  # Pick a random photo from it's file name.

    return random_photo_name  # Returns the random photo name.


def return_error_response(error_code):
    # Calculate our start and end break points, from the given error_code variable.

    error_start = str(f'<{error_code}>')
    error_end = str(f'<br {error_code}>')

    error_code_text = []  # Initialise a new list to store all of the error code text in which we wish to output.

    read_this_line = False  # Initialise read_this_line variable. Determines if python should print the specific line.

    # generate a new file object from error_codes.txt & call it's  __enter__ function.

    with open('miwell-flask-app/flaskr/static/error_handling/error_codes.txt', 'r') as error_codes:

        for skippable_line in error_codes:  # Skim over every line until we find 'error_start'.
            if error_start in skippable_line:  # If we find the error_start...
                read_this_line = True  # ...Set 'read this line' to True.

                if read_this_line:  # We can then execute the following code to read the lines.
                    for lines_to_read in error_codes:  # Start a fresh loop from this point.

                        if error_end in lines_to_read:  # If we find the line indication our error_end...
                            read_this_line = False  # ...Set 'read this line' back to False.
                            break  # Then, break out of loop.

                        else:  # Otherwise, print the line to console.
                            error_code_text.append(lines_to_read)

    if not error_code_text:  # If error_code_text returns an empty set, output the following:
        error_code_text = f"Error Code {error_code}: There is no documentation for this particular error code!"

    return error_code_text


def error_page(error_code):
    random_error_remark = generate_error_remark()
    random_error_photo = generate_error_photo()
    error_response = return_error_response(error_code)

    kwargs = {
        "title": f"Error Code: {error_code}",
        "random_error_remark": random_error_remark,
        "random_error_photo": random_error_photo,
        "error_response": error_response
    }

    return render_template('/error_handling/error_template.html', **kwargs), error_code


# Errors ----------------------------------------------------------------------------------

@current_app.errorhandler(400)
def page_400(error):
    return error_page(400)


@current_app.errorhandler(401)
def page_401(error):
    return error_page(401)


@current_app.errorhandler(403)
def page_403(error):
    return error_page(403)


@current_app.errorhandler(404)
def page_404(error):
    return error_page(404)


@current_app.errorhandler(500)
def page_500(error):
    return error_page(500)


@current_app.errorhandler(502)
def page_502(error):
    return error_page(502)


@current_app.errorhandler(503)
def page_503(error):
    return error_page(503)


@current_app.errorhandler(504)
def page_504(error):
    return error_page(504)


# Routes ----------------------------------------------------------------------------------


# In our custom test framework, we need to define a method for shutting down our server without having to press CTRL+C.
# We can do this by calling a function within the WSGI environment named 'werkzeug.server.shutdown.'

@error_handling_bp.route('/shutdown')
def server_shutdown():
    if not current_app.config['ENV'] == 'Testing':  # If the app isn't in a test configuration, then...
        abort(404)  # Refuse access to this route. Here, we 'pretend' that there is no url for our app called /shutdown.

    shutdown = request.environ.get('werkzeug.server.shutdown')

    # If we cannot get the function from our WGSI environ, raise a runtime error.
    # The runtime error is used to indicate a specific error that doesn't fall into an other error category.

    if shutdown is None:
        raise RuntimeError("No function named 'werkzeug.server.shutdown' in the WSGI environment:")

    shutdown()  # If everything else is in order, shutdown the server using werkzeug.server.shutdown.
    return 'Shutting down the test server...'
