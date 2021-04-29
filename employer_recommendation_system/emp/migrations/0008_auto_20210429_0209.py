# Generated by Django 3.2 on 2021-04-29 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0007_auto_20210429_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='emp.company'),
        ),
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
        migrations.CreateModel(
            name='AppliedJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp.job')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp.student')),
            ],
        ),
    ]
