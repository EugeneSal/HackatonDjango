# Generated by Django 2.2.9 on 2021-08-28 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Heroes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_class', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('nick_name', models.CharField(max_length=128)),
                ('hero_strength', models.IntegerField(default=40)),
                ('hero_stamina', models.IntegerField(default=80)),
                ('hero_armor', models.IntegerField(default=30)),
            ],
        ),
        migrations.CreateModel(
            name='Druid',
            fields=[
                ('heroes_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='game.Heroes')),
                ('default_strength', models.IntegerField(default=20)),
                ('default_stamina', models.IntegerField(default=100)),
                ('default_armor', models.IntegerField(default=50)),
            ],
            bases=('game.heroes',),
        ),
        migrations.CreateModel(
            name='Paladin',
            fields=[
                ('heroes_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='game.Heroes')),
                ('default_strength', models.IntegerField(default=40)),
                ('default_stamina', models.IntegerField(default=80)),
                ('default_armor', models.IntegerField(default=30)),
            ],
            bases=('game.heroes',),
        ),
        migrations.CreateModel(
            name='Warrior',
            fields=[
                ('heroes_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='game.Heroes')),
                ('default_strength', models.IntegerField(default=80)),
                ('default_stamina', models.IntegerField(default=50)),
                ('default_armor', models.IntegerField(default=40)),
            ],
            bases=('game.heroes',),
        ),
        migrations.CreateModel(
            name='Things',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_class', models.CharField(default='Меч', max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('thing_strength', models.IntegerField()),
                ('thing_stamina', models.IntegerField()),
                ('thing_armor', models.IntegerField()),
                ('owners', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='things', to='game.Heroes')),
            ],
        ),
    ]
