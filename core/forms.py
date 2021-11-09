from django.forms import ModelForm
from core.models import blog
# from django.core.exceptions import ValidationError
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# , UsernameField

# User = get_user_model()






class BlogForms(ModelForm):
    class Meta:
        model = blog
        fields = "__all__"



class userform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = "__all__"



# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ("username",'email','firsname', 'lastname')
