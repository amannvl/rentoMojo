from django.contrib import admin

# Register your models here.
from .models import Phonebook

admin.site.register(Phonebook)
