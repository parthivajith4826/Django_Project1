from django.db import models

# Create your models here.


    

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='books')

    def __str__(self):
        return f"Titlle - {self.title} Author - {self.author} Published_date - {self.published_date}"

    


class Users(models.Model):
    email = models.EmailField(max_length=75,unique=True)
    password = models.CharField(max_length=65)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return f"email - {self.email} password - {self.password}"


    


    
