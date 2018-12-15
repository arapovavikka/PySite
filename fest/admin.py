from django.contrib import admin
from .models import User, Post, Country, City, Craftsman, Organizator

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Organizator)
admin.site.register(Craftsman)

admin.site.register(Country)
admin.site.register(City)