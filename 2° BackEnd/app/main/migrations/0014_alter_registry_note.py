# Generated by Django 4.2.1 on 2023-10-15 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_registry_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registry',
            name='note',
            field=models.CharField(choices=[('3', 'Horrible'), ('5', 'Meh'), ('7', 'Fine'), ('8', 'Good'), ('9', 'Great'), ('10', 'Incredible')], default=None, max_length=30, null=True),
        ),
    ]
