# Generated by Django 4.0.5 on 2022-07-04 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_patientprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profiles/patients'),
        ),
    ]
