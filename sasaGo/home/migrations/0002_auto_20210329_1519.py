# Generated by Django 3.1.7 on 2021-03-29 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicle',
            options={'verbose_name': 'Vehicles'},
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='Description',
            new_name='description',
        ),
    ]
