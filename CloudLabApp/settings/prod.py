import os
from .settings import *

SECRET_KEY = os.environ('SECRETE_KEY')

DEBUG = False

ALLOWED_HOSTS = []