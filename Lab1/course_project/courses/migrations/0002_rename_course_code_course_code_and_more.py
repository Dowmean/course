# Generated by Django 5.1.3 on 2024-12-02 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_name',
            new_name='name',
        ),
    ]
