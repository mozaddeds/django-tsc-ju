# Generated by Django 3.2.11 on 2022-01-30 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0011_alter_guest_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.IntegerField(max_length=12, null=True)),
                ('time', models.DateTimeField()),
                ('id', models.AutoField(max_length=3, primary_key=True, serialize=False)),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='office.teacher')),
            ],
        ),
    ]
