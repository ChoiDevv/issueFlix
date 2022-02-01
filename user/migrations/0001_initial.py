# Generated by Django 4.0.1 on 2022-01-31 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=256)),
                ('nickname', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]