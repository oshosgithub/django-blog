from django.forms import ModelForm #to create a Form

#to create a form for registering user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#from internal 
from .models import Blog


#making form for CRUD
class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'


#------------------------------------------------------------------------

#making form for user registration
class RegisterUser(UserCreationForm):
   class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2',]
             #this fields are buid-in attribute from django User model.

#------------------------------------------------------------------------------- 