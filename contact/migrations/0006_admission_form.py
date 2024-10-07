# Generated by Django 4.1.5 on 2023-06-15 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_rename_calender_cancer_fullname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission_Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='image/')),
                ('father_name', models.CharField(max_length=50)),
                ('date_of_birth', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('caste', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]
