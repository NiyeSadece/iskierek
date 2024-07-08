# Generated by Django 4.2.13 on 2024-07-08 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiscordUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('discord_id', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('exp', models.IntegerField(default=0)),
                ('lvl', models.IntegerField(default=0)),
            ],
        ),
    ]
