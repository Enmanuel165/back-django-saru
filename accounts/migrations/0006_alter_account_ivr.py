# Generated by Django 5.0.7 on 2024-07-27 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_account_email_alter_account_ivr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='ivr',
            field=models.CharField(max_length=20),
        ),
    ]
