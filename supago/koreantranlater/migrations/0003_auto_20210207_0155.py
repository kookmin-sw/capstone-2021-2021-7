# Generated by Django 3.1.5 on 2021-02-07 01:55

from django.db import migrations, models
import koreantranlater.models


class Migration(migrations.Migration):

    dependencies = [
        ('koreantranlater', '0002_auto_20210131_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='koreantranslaterrequest',
            name='photo',
            field=models.FileField(upload_to=koreantranlater.models.translate_request_filename),
        ),
    ]
