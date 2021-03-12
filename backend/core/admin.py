# Register your models here.
from django.contrib import admin

from backend.core.models import Account, User

admin.site.register(User)
admin.site.register(Account)
