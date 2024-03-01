from .base import *  # noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default='pNGQDQCh96xAZfZLirgVqwgzDTHUCFYFxP5MzJwuUrmLp7FlyQw',
)
# django-insecure-)ni3((*!l%p5t2*!_q!l=*ys%%w(y1d0(&+cluvx-mthn)%ggo

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ['http://localhost:8080']
