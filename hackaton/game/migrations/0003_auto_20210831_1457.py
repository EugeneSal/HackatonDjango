# Generated by Django 2.2.9 on 2021-08-31 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_things_used'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='heroes',
            options={'ordering': ('name_class',)},
        ),
        migrations.AddField(
            model_name='heroes',
            name='hp',
            field=models.IntegerField(default=1000),
        ),
    ]