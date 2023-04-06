from django.contrib.auth.models import User,Group
from .models import *
from django.core.cache import cache
def custom_commands(command:str):
    """
    This function taked command as string input,
    It just executes all your written commands from this file,
    The reason for this is to make your views.py cleaner,
    By importing most functions in another file and use when needed
    """
    exec(command)

def cache_object_set(key:str,value:any,Default_Timeout:int=None,NX:bool=False):
    """
    Function to set object in cache,
    both NX and EX methods are supported,
    """
    if NX:
        cache.add(key,value,Default_Timeout)
    else:
        cache.set(key,value,Default_Timeout)

def cache_object_get_or_set(key:str,value:any,Default_Timeout:int=None):
    """
    Get or Set, If value doesn't exist in cache it creates the value,
    If value already exists in cache it just retrieves it
    """
    return cache.get_or_set(key,value,Default_Timeout)

def add_to_students(users):
    gro=Group.objects.get(name="students")
    users.groups.add(gro)

def add_to_staff(users):
    gro=Group.objects.get(name="staff")
    users.groups.add(gro)

def user_group(users,group):
    return users.groups.filter(name=group).exists()

def object_exists(factor,model):
    # factor is a dictionary {"email":"abc@ghmail.com"} < usage is here, arguments are supposed to be passed like this
    # Model is supposed to be passed as a string object like model="User" where User is the name of the model you are refering to
    return eval(model).objects.filter(**factor).exists() 
def validate_name(name):
    if name!=name.capitalize():
        return True
    else:
        return False

def object_creator(factor,model):
    eval(model).objects.create(**factor)

def object_filter(factor,model):
    # factor is a dictionary {"email":"abc@ghmail.com"} < usage is here, arguments are supposed to be passed like this
    # Model is supposed to be passed as a string object like model="User" where User is the name of the model you are refering to
    return eval(model).objects.filter(**factor)
def object_get(factor:dict,model):
    # factor is a dictionary {"email":"abc@ghmail.com"} < usage is here, arguments are supposed to be passed like this
    # Model is supposed to be passed as a string object like model="User" where User is the name of the model you are refering to
    return eval(model).objects.get(**factor)
def object_filter_orderby(factor,model,orderby):
    # factor is a dictionary {"email":"abc@ghmail.com"} < usage is here, arguments are supposed to be passed like this
    # Model is supposed to be passed as a string object like model="User" where User is the name of the model you are refering to
    return eval(model).objects.filter(**factor).order_by(orderby)

def object_all(model):
    # factor is a dictionary {"email":"abc@ghmail.com"} < usage is here, arguments are supposed to be passed like this
    # Model is supposed to be passed as a string object like model="User" where User is the name of the model you are refering to
    return eval(model).objects.all()

def object_remove(factor,model):
    # factor is a dictionary {"email":"abc@ghmail.com"} < usage is here, arguments are supposed to be passed like this
    # Model is supposed to be passed as a string object like model="User" where User is the name of the model you are refering to
    return eval(model).objects.filter(**factor)
