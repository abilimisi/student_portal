# Generated by Django 4.1.5 on 2023-06-29 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_admission_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission_form',
            name='gender',
            field=models.CharField(max_length=50),
        ),
    ]