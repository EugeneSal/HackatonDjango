import random as r

from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PaladinForm, WarriorForm, DruidForm, ThingsForm
from .models import *


def put_on_inventory(request, hero_id, thing_id):
    person = get_object_or_404(Heroes, id=hero_id)
    thing = get_object_or_404(Things, id=thing_id)
    if thing.used == 1:
        return redirect('person_detail', hero_id)
    person.hero_armor += thing.thing_armor
    person.hero_strength += thing.thing_strength
    person.hero_stamina += thing.thing_stamina
    person.hp = person.hero_stamina * 40
    thing.used = True
    thing.save()
    person.save()
    return redirect('person_detail', hero_id)


def take_off_inventory(request, hero_id, thing_id):
    person = get_object_or_404(Heroes, id=hero_id)
    thing = get_object_or_404(Things, id=thing_id)
    if thing.used == 0:
        return redirect('person_detail', hero_id)
    person.hero_armor -= thing.thing_armor
    person.hero_strength -= thing.thing_strength
    person.hero_stamina -= thing.thing_stamina
    person.hp = person.hero_stamina * 40
    thing.used = False
    thing.save()
    person.save()
    return redirect('person_detail', hero_id)


def index(request):
    person = Heroes.objects.all()
    paginator = Paginator(person, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'index.html', {'page': page, 'paginator': paginator})


def create_paladin(request):
    form = PaladinForm(request.POST or None)
    if request.method == 'GET' or not form.is_valid():
        return render(request, 'create.html',
                      {'form': form, 'paladin': True})
    paladin = form.save(commit=False)
    paladin.hero_stamina = paladin.default_stamina
    paladin.hero_armor = paladin.default_armor
    paladin.hero_strength = paladin.default_strength
    paladin.name_class = 'Паладин'
    paladin.save()
    return redirect('index')


def create_druid(request):
    form = DruidForm(request.POST or None)
    if request.method == 'GET' or not form.is_valid():
        return render(request, 'create.html',
                      {'form': form, 'druid': True})
    druid = form.save(commit=False)
    druid.hero_stamina = druid.default_stamina
    druid.hero_armor = druid.default_armor
    druid.hero_strength = druid.default_strength
    druid.name_class = 'Друид'
    druid.save()
    return redirect('index')


def create_warrior(request):
    form = WarriorForm(request.POST or None)
    if request.method == 'GET' or not form.is_valid():
        return render(request, 'create.html',
                      {'form': form, 'warrior': True})
    warrior = form.save(commit=False)
    warrior.hero_stamina = warrior.default_stamina
    warrior.hero_armor = warrior.default_armor
    warrior.hero_strength = warrior.default_strength
    warrior.name_class = 'Воин'
    warrior.save()
    return redirect('index')


def create_things(request):
    form = ThingsForm(request.POST or None)
    if request.method == 'GET' or not form.is_valid():
        return render(request, 'create.html',
                      {'form': form, 'things': True})
    thing = form.save(commit=False)
    thing.save()
    return redirect('index')


def person_detail(request, hero_id):
    person = get_object_or_404(Heroes, id=hero_id)
    person.hp = person.hero_stamina * 40
    person.save()
    things = person.things.all()
    return render(request, 'person_detail.html', {'person': person,
                                                  'things': things})


def choice_the_pair(request):
    person_list = Heroes.objects.all()
    list_person = []
    if len(person_list) < 2:
        return redirect('index')
    for i in range(len(person_list)):
        list_person.append(person_list[i])
    list_pair = []
    for i in range(0, 2):
        choice = r.choice(list_person)
        list_pair.append(choice)
        list_person.remove(choice)
    return render(request, 'choice.html', {'person_list': list_pair,
                                           'person_1': list_pair[0],
                                           'person_2': list_pair[1]})


def fight(self, damage, defence):
    defence_percent = r.randint(80, 160)
    message = ''
    if defence_percent > 130:
        message = 'Искусно блокирует'
        attack = r.randint(50, 80)
    else:
        attack = r.randint(90, 150)
    total_damage = (attack / 100) * (
            damage - (defence_percent / 100) * defence)
    if attack > 120:
        message = 'Критический удар'
    self.hp = self.hp - total_damage
    return self.hp, message


def arena(request, hero1_id, hero2_id):
    list_pair = []
    list_pair.append(get_object_or_404(Heroes, id=hero1_id))
    list_pair.append(get_object_or_404(Heroes, id=hero2_id))
    battle_log = []
    win_log = []
    while True:
        defender, attacker = r.sample(list_pair, 2)
        base_attack = attacker.hero_strength * 14
        hp_now = defender.hp
        defender.hp, message = fight(defender, base_attack, defender.hero_armor)
        hp_left = hp_now - defender.hp
        battle_log.append(f'{attacker}  наносит удар по {defender} на '
                          f'{round(hp_left)}')
        if message != '':
            if message == 'Искусно блокирует':
                battle_log[-1] += f',  но   {defender.name}'
            battle_log.append(message)
        battle_log.append(f'У {defender} {round(defender.hp)} '
                          f'осталось пунктов жизни')
        if defender.hp < 0:
            break
    win_log.append(f'{defender} умирает --- победил {attacker}')
    win_log.append(f'У {attacker} осталось {round(attacker.hp)} жизни')
    return render(request, 'arena.html', {'person_list': list_pair,
                                          'logs': battle_log,
                                          'win_log': win_log})
