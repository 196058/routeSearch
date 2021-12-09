from django.contrib import admin
from .models import Mecainfo, User


model = [User, Mecainfo]
admin.site.register(model)
