from django.contrib.auth.models import User,Group
from .models import *

def add_to_students(users):
    gro=Group.objects.get(name="students")
    users.groups.add(gro)

def add_to_staff(users):
    gro=Group.objects.get(name="staff")
    users.groups.add(gro)

def duplicate_entries_preventer(factor,model):
    # factor is a dictionary {"email":"abc@ghmail.com"} < usage is here, arguments are supposed to be passed like this
    # Model is supposed to be passed as a string object like model="User" where User is the name of the model you are refering to
    if eval(model).objects.filter(**factor).exists():
        return True
    else:
        return False

def validate_name(name):
    if name!=name.capitalize():
        return True
    else:
        return False
def object_creator(factor,model):
    eval(model).objects.create(**factor)