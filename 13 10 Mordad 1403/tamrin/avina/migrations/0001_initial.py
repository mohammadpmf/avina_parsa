# Generated by Django 5.0.4 on 2024-07-22 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=225)),
                ('last_name', models.CharField(max_length=225)),
                ('birth_date', models.DateField()),
                ('country', models.CharField(max_length=225)),
                ('city', models.CharField(max_length=225)),
                ('postal_code', models.CharField(max_length=225)),
                ('number', models.IntegerField()),
            ],
        ),
    ]
