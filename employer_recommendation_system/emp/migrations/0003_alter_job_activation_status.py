# Generated by Django 3.2 on 2021-05-19 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0002_auto_20210519_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='activation_status',
            field=models.IntegerField(choices=[(None, '--------'), (1, 'Active'), (3, 'Deactive')], max_length=10),
        ),
    ]
