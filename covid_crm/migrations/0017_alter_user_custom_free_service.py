# Generated by Django 3.2 on 2021-04-30 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid_crm', '0016_user_custom_free_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_custom',
            name='free_service',
            field=models.BooleanField(),
        ),
    ]
