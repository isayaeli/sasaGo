# Generated by Django 3.1.7 on 2021-04-01 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210401_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='vehicles',
            field=models.ManyToManyField(related_name='List_booking', to='home.BookedVehicle'),
        ),
    ]