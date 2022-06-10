from django import forms
from .models import Tasks, Category
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        # fields = '__all__'
        fields = ['title', 'category', 'user']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control no-border', 'placeholder': 'Add an item...'})
        }

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control no-border', 'placeholder': 'Add an item...'})
        }

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'create-category', 'placeholder': 'Add category...', 'id': 'create_category'})
        }

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'content']
        widgets = {
            'content': forms.TextInput(attrs={'rows':4, 'cols':40}),
            'title': forms.TextInput(attrs={'class': 'form-control'})

        }