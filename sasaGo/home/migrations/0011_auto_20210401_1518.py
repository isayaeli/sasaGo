# Generated by Django 3.1.7 on 2021-04-01 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20210401_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargoinfo',
            name='booking_info_for',
        ),
        migrations.RemoveField(
            model_name='cargoinfo',
            name='vehicle',
        ),
        migrations.AddField(
            model_name='cargoinfo',
            name='booking',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.bookings'),
        ),
    ]