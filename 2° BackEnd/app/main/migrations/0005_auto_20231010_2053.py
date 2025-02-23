# Generated by Django 4.2.1 on 2023-10-10 23:53

from django.db import migrations
from main.management.commands.seeds import numberOfComments

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_user_friend'),
    ]

    operations = [
        migrations.RunSQL(
            f'ALTER SEQUENCE main_comment_id_seq RESTART WITH {numberOfComments + 1};'
        )
    ]
