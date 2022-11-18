from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import 

class CreateUserForm(UserCreationForm):
    class Meta:
        pass
        model = User
        fields = ["username","email","password1","password2"]

