# Generated by Django 4.2.6 on 2023-10-29 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_entity_registration_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='registration_number',
            field=models.FloatField(null=True),
        ),
    ]
