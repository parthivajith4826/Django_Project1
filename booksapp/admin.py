from django.contrib import admin
from .models import Book,Users,Category

# Register your models here

admin.site.register(Book)
admin.site.register(Users)
admin.site.register(Category)