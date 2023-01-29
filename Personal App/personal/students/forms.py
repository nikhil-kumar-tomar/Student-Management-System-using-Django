from django import forms
from django.forms import ModelForm
from .models import studs,attendance
from .miscellaneous import validate_name
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class roll_s(forms.Form):
    roll=forms.IntegerField(label="Your Roll No: ")
class indexes(forms.Form):
    Choices = [
    ('see_all', 'see all Students in the Database'),
    ('search', 'Search Specific students'),
    ('ent_info', 'Enter Information for students to be registered'),
    ('update','Update already exisitng database'),
    ]

    choice=forms.ChoiceField(choices=Choices,widget=forms.RadioSelect)
class ent_infos(ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'style':'width:10%'}),max_length=400)
    class Meta():
        model=studs
        fields=['name','email']

    def clean(self):
        cleaned_data=super().clean()
        if validate_name(cleaned_data['name']):
            raise forms.ValidationError("The first word of your name is not capitalized")
class user_create(UserCreationForm):
    first_name=forms.CharField(max_length=300,required=True)
    last_name=forms.CharField(max_length=300,required=True)
    class Meta():
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
class user_sign(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'style':'width:10%'}),max_length=400)
    password=forms.CharField(widget=forms.PasswordInput(attrs={'style':'width:10%'}),max_length=400)
class take_attend(forms.Form):
    attend=forms.BooleanField(widget=forms.CheckboxInput(attrs={"style":"allignment:centre"}),required=False)