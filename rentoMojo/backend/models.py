from django.db import models
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db import models

class Phonebook(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True, blank=False)

    def __str__(self):
        return self.name

