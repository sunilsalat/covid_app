# Generated by Django 3.2 on 2021-04-29 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid_crm', '0007_tiffin_service_provider_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiffin_service_provider',
            name='tiffin_image',
            field=models.ImageField(blank=True, null=True, upload_to='tf_image'),
        ),
    ]