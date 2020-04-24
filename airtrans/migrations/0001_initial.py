# Generated by Django 2.2 on 2020-03-12 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('airport_code', models.IntegerField(max_length=6, primary_key=True, serialize=False)),
                ('airport_name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('coordinates', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('book_ref', models.AutoField(primary_key=True, serialize=False)),
                ('book_date', models.DateTimeField(auto_now_add=True)),
                ('total_amount', models.FloatField()),
            ],
        ),
    ]