# Configures our gunicorn file

import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1  # Dynamically generates workers.
bind = 'unix:miwell-flask-app.sock'  # Create and bind to a unix socket file within the cwd.
umask = 0o007
reload = True

# logging
accesslog = '-'
errorlog = '-'
