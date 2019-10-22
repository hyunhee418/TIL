from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm

from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email',)

class CustomAuthenticationForm(AuthenticationForm):

    class Meta:
        model = User