# Generated by Django 4.2.5 on 2023-09-22 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('rating', models.IntegerField()),
                ('genre', models.CharField(max_length=200)),
                ('image', models.ImageField(default='', upload_to='')),
            ],
        ),
    ]
