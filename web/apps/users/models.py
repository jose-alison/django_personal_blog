from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_reader = models.BooleanField('Colunista', default=False)
    is_publisher = models.BooleanField('Publicador', help_text='Pode publicar?', default=False)

    class Meta:
        db_table = 'users'
