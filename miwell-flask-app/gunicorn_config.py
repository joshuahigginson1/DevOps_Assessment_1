# Configures our gunicorn file

import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1  # Dynamically generates workers.

bind = 'unix:/opt/miwell-flask-app/miwell-gunicorn-socket.sock'
umask = 0o007
reload = True

# logging
accesslog = '-'
errorlog = '-'
