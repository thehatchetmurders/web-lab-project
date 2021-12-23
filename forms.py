from .models import Comments, Messages, Consult
from django.forms import ModelForm, TextInput, Textarea, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ["name","email","comment"]
        widgets = {"name": TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'id': 'name'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'type': 'email',
                'id': 'email'
            }),
            "comment": Textarea(attrs={
                'name': "",
                'id': 'message',
                'cols': '30',
                'rows': '10',
                'class': 'form-control'
            })
        }

class MessagesForm(ModelForm):
    class Meta:
        model = Messages
        fields = ["name","email","subject","message"]
        widgets = {
            "name": TextInput(attrs={
                'type' : 'text',
                'class': 'form-control',
                'placeholder': 'Your Name'
            }),
            "email": TextInput(attrs={
                'type' : 'text',
                'class': 'form-control',
                'placeholder': 'Your Email'
            }),
            "subject": TextInput(attrs={
                'type' : 'text',
                'class': 'form-control',
                'placeholder': 'Subject'
            }),
            "message": Textarea(attrs={
                'name':'',
                'id':'',
                'cols':'30',
                'rows':'7',
                'class':'form-control',
                'placeholder':'Message'
            })
        }

class ConsultsForm(ModelForm):
    class Meta:
        model = Consult
        fields = ["name","surname","age","phone","date","time","comment"]
        widgets = {
            "name": TextInput(attrs={
                'type' : 'text',
                'class': 'form-control',
                'placeholder': 'First name'
            }),
            "surname": TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Last name'
            }),
            "age": TextInput(attrs={
                'type': 'number',
                'class': 'form-control',
                'placeholder': 'Age'
            }),
            "phone": TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Phone number'
            }),
            "date": TextInput(attrs={
                'type' : 'date',
                'class': 'form-control',
                'placeholder': 'Date'
            }),
            "time": TextInput(attrs={
                'type' : 'time',
                'class': 'form-control',
                'placeholder': 'time'
            }),
            "comment": Textarea(attrs={
                'name':'',
                'id':'',
                'cols':'30',
                'rows':'2',
                'class':'form-control',
                'placeholder':'Message'
            })
        }


# class AccountsForm(ModelForm):
#     class Meta:
#         model = Account
#         fields = ["full_name","email","ph_num","password", "client_ID"]
#         widgets = {
#             "full_name": TextInput(attrs={
#                 'type' : 'text',
#                 'class': 'input100',
#                 'placeholder': 'Full name'
#             }),
#             "email": TextInput(attrs={
#                 'type': 'text',
#                 'class': 'input100',
#                 'placeholder': 'Email addess...'
#             }),
#             "ph_num": TextInput(attrs={
#                 'type': 'text',
#                 'class': 'input100',
#                 'placeholder': 'Phone number'
#             }),
#             "client_ID": TextInput(attrs={
#                 'type': 'text',
#                 'class': 'input100',
#                 'placeholder': 'Your name'
#             }),
#             "password": TextInput(attrs={
#                 'type' : 'password',
#                 'class': 'input100',
#                 'placeholder': '*************'
#             })
#         }

