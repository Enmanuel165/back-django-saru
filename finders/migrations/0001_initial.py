# Generated by Django 5.0.6 on 2024-06-07 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default=str, max_length=254)),
                ('password', models.CharField(max_length=200)),
                ('type_acot', models.CharField(max_length=1)),
            ],
        ),
    ]
