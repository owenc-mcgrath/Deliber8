# Generated by Django 5.1 on 2024-08-31 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PNM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('resume', models.FileField(upload_to='resumes/')),
                ('photo', models.ImageField(upload_to='photos/')),
                ('score', models.FloatField(default=0.0)),
            ],
        ),
    ]
