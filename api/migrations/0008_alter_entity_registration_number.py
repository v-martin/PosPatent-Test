# Generated by Django 4.2.6 on 2023-10-29 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_usefulmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='registration_number',
            field=models.FloatField(null=True),
        ),
    ]