# Generated by Django 3.2.6 on 2021-09-04 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_remove_job_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(),
        ),
    ]