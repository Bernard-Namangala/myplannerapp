# Generated by Django 2.2.7 on 2019-11-21 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myplanner', '0005_auto_20191118_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote_text', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=250)),
            ],
        ),
    ]
