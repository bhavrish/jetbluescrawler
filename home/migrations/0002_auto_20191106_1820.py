# Generated by Django 2.2 on 2019-11-06 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LegroomBadModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=1000)),
                ('date', models.DateTimeField()),
                ('prediction_level', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LegroomGoodModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=1000)),
                ('date', models.DateTimeField()),
                ('prediction_level', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TimelinessBadModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=1000)),
                ('date', models.DateTimeField()),
                ('prediction_level', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TimelinessGoodModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=1000)),
                ('date', models.DateTimeField()),
                ('prediction_level', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameModel(
            old_name='Timeliness',
            new_name='AvailabilityBadModel',
        ),
        migrations.RenameModel(
            old_name='Cost',
            new_name='AvailabilityGoodModel',
        ),
        migrations.RenameModel(
            old_name='Legroom',
            new_name='CostBadModel',
        ),
        migrations.RenameModel(
            old_name='Availability',
            new_name='CostGoodModel',
        ),
    ]
