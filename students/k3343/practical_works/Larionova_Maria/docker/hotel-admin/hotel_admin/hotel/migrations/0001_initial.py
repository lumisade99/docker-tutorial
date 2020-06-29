# Generated by Django 3.0.6 on 2020-06-29 21:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Challengers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('passport', models.IntegerField()),
                ('birthdate', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('city_from', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('passport', models.IntegerField()),
                ('position', models.CharField(choices=[('1', 'Administrator'), ('2', 'Servant')], default='2', max_length=1)),
                ('user', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(choices=[('1', '1 person'), ('2', '2 persons'), ('3', '3 persons')], default='1', max_length=1)),
                ('room_state', models.CharField(choices=[('1', 'Free'), ('2', 'Not free')], default='1', max_length=1)),
                ('price', models.IntegerField()),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Floor')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('state', models.CharField(choices=[('1', 'Not hired'), ('2', 'Hired')], default='1', max_length=1)),
                ('administrator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Employee')),
                ('challenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Challengers')),
            ],
        ),
        migrations.CreateModel(
            name='ClientRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Client')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Room')),
            ],
        ),
        migrations.CreateModel(
            name='Cleaning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Employee')),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Floor')),
            ],
        ),
    ]
