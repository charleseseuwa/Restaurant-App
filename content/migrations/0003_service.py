# Generated by Django 4.2 on 2023-04-30 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_subscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
