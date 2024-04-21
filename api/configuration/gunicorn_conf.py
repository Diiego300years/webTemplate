import os
#
wsgi_app = "api.wsgi:app"
#
# ## For Flask-SocketIO should be only 1 worker
# workers = int(os.environ.get('GUNICORN_PROCESSES', '1'))



# # With this could be fun giving more and more xD
# threads = int(os.environ.get('GUNICORN_THREADS', '4'))
#
# timeout = int(os.environ.get('GUNICORN_TIMEOUT', '120'))
#
# # Binding port 5000
bind = os.environ.get('GUNICORN_BIND', '0.0.0.0:8000')
#
# # Only localhost for now, in future * for all ips
forwarded_allow_ips = '*'
proxy_allow_ips = '*'

# # # What should headers have

reload = True

# timeout = 120
# keepalive = 25

# secure_scheme_headers = {
#             'X-Forwarded-Proto': 'https',
#             'X-Forwarded-SSL': 'on',
#             'X-Forwarded-PROTOCOL': 'ssl',
#             'Access-Control-Allow-Origin': '*',
#             'Access-Control-Allow-Credentials': 'true',
# }

# # Info is not the most important. For future maybe 2 handlers or sth
loglevel = "debug"
#
# # Optional ssl, for prod must 2 == require, for now optional
cert_reqs = 0
#
# # reload worker if there's code change
# # reload = 'auto' maybe in future, for now debbuger and volumins should provide it

# Set True if you want to see if config is okay. Return 0 mean it's okay
# check_config = False

# Better visualization
# print_config = True
#
accesslog = '-'
#
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# certfile = '/app/127.0.0.1.pem'
# keyfile = '/app/127.0.0.1-key.pem'
cors_allowed_origins = '*'

access_control_allow_credentials = False