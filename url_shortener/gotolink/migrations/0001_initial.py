# Generated by Django 3.2.9 on 2021-11-09 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='urls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('og_link', models.CharField(max_length=1000)),
                ('new_link', models.CharField(max_length=20)),
            ],
        ),
    ]