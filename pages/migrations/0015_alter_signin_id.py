# Generated by Django 4.2.1 on 2023-05-28 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_alter_signin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
