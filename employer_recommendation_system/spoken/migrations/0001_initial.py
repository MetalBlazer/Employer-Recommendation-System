# Generated by Django 3.2 on 2021-05-18 13:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_code', models.CharField(max_length=100, unique=True)),
                ('institution_name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('pincode', models.PositiveIntegerField()),
                ('resource_center', models.BooleanField()),
                ('rating', models.PositiveSmallIntegerField()),
                ('contact_person', models.TextField()),
                ('remarks', models.TextField()),
                ('status', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'events_academiccenter',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'events_department',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'events_district',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FossCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foss', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('status', models.IntegerField()),
                ('user_id', models.BigIntegerField()),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('is_learners_allowed', models.IntegerField()),
                ('show_on_homepage', models.PositiveSmallIntegerField()),
                ('is_translation_allowed', models.IntegerField()),
                ('available_for_nasscom', models.IntegerField()),
            ],
            options={
                'db_table': 'creation_fosscategory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FossMdlCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mdlcourse_id', models.PositiveIntegerField()),
                ('mdlquiz_id', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'events_fossmdlcourses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InstituteType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'events_institutetype',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Invigilator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'events_invigilator',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('pincode', models.PositiveIntegerField()),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'events_location',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Organiser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'events_organiser',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmation_code', models.CharField(max_length=255)),
                ('street', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('pincode', models.PositiveIntegerField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('picture', models.CharField(blank=True, max_length=100, null=True)),
                ('thumb', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField()),
            ],
            options={
                'db_table': 'cms_profile',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpokenCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'events_city',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpokenState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('longtitude', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('img_map_area', models.TextField()),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('has_map', models.IntegerField()),
            ],
            options={
                'db_table': 'events_state',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpokenStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=15)),
                ('verified', models.PositiveSmallIntegerField()),
                ('error', models.IntegerField()),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'events_student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpokenUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=75)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_code', models.CharField(max_length=100)),
                ('tdate', models.DateField()),
                ('ttime', models.TimeField()),
                ('status', models.PositiveSmallIntegerField()),
                ('participant_count', models.PositiveIntegerField()),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'events_test',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TestAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mdluser_firstname', models.CharField(max_length=100)),
                ('mdluser_lastname', models.CharField(max_length=100)),
                ('mdluser_id', models.PositiveIntegerField()),
                ('mdlcourse_id', models.PositiveIntegerField()),
                ('mdlquiz_id', models.PositiveIntegerField()),
                ('mdlattempt_id', models.PositiveIntegerField()),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('count', models.PositiveSmallIntegerField()),
                ('status', models.PositiveSmallIntegerField()),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'events_testattendance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TestCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'events_testcategory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TrainingRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_planner', models.BigIntegerField()),
                ('sem_start_date', models.DateField()),
                ('training_start_date', models.DateField(default=datetime.datetime.now)),
                ('training_end_date', models.DateField(default=datetime.datetime.now)),
                ('course', models.BigIntegerField()),
                ('batch', models.BigIntegerField()),
                ('participants', models.PositiveIntegerField(default=0)),
                ('course_type', models.PositiveIntegerField(default=None)),
                ('status', models.PositiveSmallIntegerField(default=0)),
                ('cert_status', models.PositiveSmallIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'events_trainingrequest',
                'managed': False,
            },
        ),
    ]
