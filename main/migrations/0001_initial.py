# Generated by Django 3.1.4 on 2020-12-10 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='pics')),
                ('Description', models.TextField()),
                ('Season', models.IntegerField()),
                ('Episode', models.IntegerField()),
            ],
        ),
    ]
