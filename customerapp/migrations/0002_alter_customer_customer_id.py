# Generated by Django 3.2.7 on 2021-09-08 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
