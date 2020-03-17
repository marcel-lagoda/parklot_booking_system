# Generated by Django 2.2 on 2020-03-17 01:32

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
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(unique=True)),
                ('arrival', models.DateField()),
                ('departure', models.DateField()),
                ('no_of_people', models.PositiveSmallIntegerField(default=1)),
                ('status', models.CharField(choices=[('NEW', 'NEW'), ('CANCELLED', 'CANCELLED')], max_length=16)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
