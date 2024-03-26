from django.contrib import admin

from .models import Restaurant, Review
from django.contrib.auth.models import User

admin.site.register(Restaurant)
admin.site.register(Review)
admin.site.register(User)

