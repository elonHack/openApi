# Generated by Django 4.2.5 on 2023-09-13 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
