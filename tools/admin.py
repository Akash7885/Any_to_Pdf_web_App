from django.contrib import admin
from . models import UserFile ,UserFeedback

# Register your models here.
admin.site.register(UserFile)
admin.site.register(UserFeedback)