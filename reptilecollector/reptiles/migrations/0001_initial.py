# Generated by Django 5.0.1 on 2024-02-06 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reptile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
    ]
