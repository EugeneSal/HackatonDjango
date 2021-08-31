from django.db import models


class Heroes(models.Model):
    name_class = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    nick_name = models.CharField(max_length=128)
    hero_strength = models.IntegerField(default=40)
    hero_stamina = models.IntegerField(default=80)
    hero_armor = models.IntegerField(default=30)
    hp = models.IntegerField(default=1000)
    alive = models.BooleanField(default=True)

    class Meta:
        ordering = ('name_class',)

    def __str__(self):
        return f'{self.name_class} {self.name} {self.nick_name}'


class Paladin(Heroes):
    default_strength = models.IntegerField(default=40)
    default_stamina = models.IntegerField(default=80)
    default_armor = models.IntegerField(default=30)

    def __str__(self):
        return (f'{self.name_class} {self.name} {self.nick_name}\n'
                f'Характеристики: '
                f'Сила  {self.hero_strength}\n'
                f'Выносливость  {self.hero_stamina}\n'
                f'Броня  {self.hero_armor}')


class Druid(Heroes):
    # name_class = models.CharField(default='Друид-медведь', max_length=128)
    default_strength = models.IntegerField(default=20)
    default_stamina = models.IntegerField(default=100)
    default_armor = models.IntegerField(default=50)

    def __str__(self):
        return (f'{self.name_class} {self.name} {self.nick_name}\n'
                f'Характеристики: '
                f'Сила  {self.hero_strength}\n'
                f'Выносливость  {self.hero_stamina}\n'
                f'Броня  {self.hero_armor}')


class Warrior(Heroes):
    # name_class = models.CharField(default='Воин', max_length=128)
    default_strength = models.IntegerField(default=80)
    default_stamina = models.IntegerField(default=50)
    default_armor = models.IntegerField(default=40)

    def __str__(self):
        return (f'{self.name_class} {self.name} {self.nick_name}\n'
                f'Характеристики: '
                f'Сила  {self.hero_strength}\n'
                f'Выносливость  {self.hero_stamina}\n'
                f'Броня  {self.hero_armor}')


class Things(models.Model):
    owners = models.ForeignKey(Heroes, on_delete=models.CASCADE,
                               related_name='things', blank=True, null=True)
    name_class = models.CharField(default='Меч', max_length=128)
    name = models.CharField(max_length=128)
    thing_strength = models.IntegerField()
    thing_stamina = models.IntegerField()
    thing_armor = models.IntegerField()
    used = models.BooleanField(default=0)

    def __str__(self):
        return f'{self.name} {self.name_class}'
