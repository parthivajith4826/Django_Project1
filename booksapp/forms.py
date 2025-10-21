from django import forms
from .models import Book,Users,Category
import hashlib





class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ("title","author","published_date","category")
        widgets = {

            'published_date':forms.DateInput(attrs={'type':'date'})
        }
class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name']


class SignupForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ("email","password")
        widgets = {

            'password' : forms.PasswordInput()
        }

    def clean_email(self):
        email = self.cleaned_data.get('email','').strip()
        


        if Users.objects.filter(email=email).exists():
            raise forms.ValidationError("The email is Existed")
        if '@' not in email:
            raise forms.ValidationError("Enter a valid email adress (missing @).")
        if not email.lower().endswith('@gmail.com'):
            raise forms.ValidationError('Email must be a gmail.com address')
        print(email)
        return email
    
    def clean_password(self):
        password = self.cleaned_data.get('password','')
        
        if len(password) < 8 :
            raise forms.ValidationError('Password must be at least 8 characters long.')
        if password.isdigit():
            raise forms.ValidationError("Password cannot be only numbers.")
        
        # if password.lower() or password.upper() == password:
        #     raise forms.ValidationError("Password must include both upper and lower case letters.")
        
        password = hashlib.sha256(password.encode()).hexdigest()
        print(password)
        return password
