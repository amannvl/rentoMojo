from django.urls import include, path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
  path('getphonebooks', csrf_exempt(views.get_phonebooks)),
  path('addphonebook', csrf_exempt(views.add_phonebook)),
  path('updatephonebook/<int:id>', csrf_exempt(views.update_phonebook)),
  path('deletephonebook/<int:id>', csrf_exempt(views.delete_phonebook))
]