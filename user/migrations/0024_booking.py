# Generated by Django 5.0.4 on 2024-05-16 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('train_number', models.CharField(max_length=50)),
                ('class_type', models.CharField(max_length=50)),
                ('station_from', models.CharField(max_length=50)),
                ('station_to', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('pnr', models.AutoField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
