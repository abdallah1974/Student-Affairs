# Generated by Django 4.2.1 on 2023-05-28 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_alter_signin_gpa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin',
            name='Fname',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='signin',
            name='Lname',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]