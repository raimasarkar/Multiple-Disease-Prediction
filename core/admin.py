from django.contrib import admin
from .models import User,Medical,Ment,Profile


models_list = [User,Medical,Ment,Profile]
admin.site.register(models_list)
