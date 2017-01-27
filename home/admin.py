from django.contrib import admin

from .models import Make, Model, Review

admin.site.register(Make)
admin.site.register(Model)
admin.site.register(Review)

# Register your models here.
