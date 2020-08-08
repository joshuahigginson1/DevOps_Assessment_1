# Configures our gunicorn file

import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1  # Dynamically generates workers.
bind = ['127.0.0.1:5000']  # Instructs gunicorn to listen to requests on local port 8000.
umask = 0
reload = True

# logging
accesslog = '-'
errorlog = '-'
