# Generated by Django 4.1.7 on 2023-03-31 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_rename_calendar_cancer_calender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cancer',
            old_name='name',
            new_name='username',
        ),
    ]