# Generated by Django 4.2.1 on 2023-05-28 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_rename_birthdate_student_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(default=None, null=True),
        ),
    ]