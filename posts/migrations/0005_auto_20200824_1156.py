# Generated by Django 3.0.6 on 2020-08-24 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20200728_1537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='writer',
        ),
    ]