from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.UserProfiles)
admin.site.register(models.ProfileFeedItem)
