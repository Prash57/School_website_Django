# Generated by Django 4.2.10 on 2024-03-23 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_calender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calender',
            name='calender',
            field=models.ImageField(upload_to='uploads/calender'),
        ),
    ]