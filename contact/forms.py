from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student

class StudentSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    register_number = forms.CharField(max_length=20)
    college_id = forms.CharField(max_length=20)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'register_number', 'college_id', 'profile_picture', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data.get('first_name', '')
        user.last_name = self.cleaned_data.get('last_name', '')

        if commit:
            user.save()
            # Explicitly create Student profile only if form is submitted
            Student.objects.create(
                user=user,
                register_number=self.cleaned_data['register_number'],
                college_id=self.cleaned_data['college_id'],
                profile_picture=self.cleaned_data.get('profile_picture', 'profile_pics/default.jpg')
            )

        return user
