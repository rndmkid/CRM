# Generated by Django 2.1 on 2018-11-08 19:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('desc', models.TextField(blank=True)),
                ('address_one', models.CharField(max_length=100)),
                ('address_two', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('phone', models.CharField(max_length=20)),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'accounts',
            },
        ),
    ]
