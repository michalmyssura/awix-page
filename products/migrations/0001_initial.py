# Generated by Django 2.2.3 on 2019-08-14 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('image2', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
