# Generated by Django 3.2 on 2022-03-21 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0055_alter_company_domain'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='notified_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
