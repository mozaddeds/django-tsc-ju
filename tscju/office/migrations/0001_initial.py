# Generated by Django 3.2.11 on 2022-01-26 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomNo', models.IntegerField(max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Muktomoncho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventName', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accessories', models.CharField(choices=[('Musical', 'Musical'), ('Computer', 'Computer'), ('Technology', 'Technology')], max_length=200, null=True)),
                ('sitting', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomType', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teaher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
    ]
