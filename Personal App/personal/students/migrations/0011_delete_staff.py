# Generated by Django 4.1.3 on 2023-02-27 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_staff'),
    ]

    operations = [
        migrations.DeleteModel(
            name='staff',
        ),
    ]