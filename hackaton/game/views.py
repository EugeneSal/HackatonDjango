from .models import *
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
import random as r

def put_on_inventory(request, hero_id, thing_id):
    person = get_object_or_404(Paladin, id=hero_id)
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
    person = get_object_or_404(Paladin, id=hero_id)
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
    for per in person:
        per.hp = per.hero_stamina * 40
        per.save()
    paginator = Paginator(person, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'index.html', {'page': page, 'paginator': paginator})


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
    if defence_percent > 130:
        print(f'{self.name} Искусно блокирует')
        attack = r.randint(50, 80)
    else:
        attack = r.randint(90, 150)
    total_damage = (attack / 100) * (
            damage - (defence_percent / 100) * defence)
    if attack > 120:
        print('Критический удар')
    self.hp = self.hp - total_damage


def arena(request, hero1_id, hero2_id):
    list_pair = []
    list_pair.append(get_object_or_404(Heroes, id=hero1_id))
    list_pair.append(get_object_or_404(Heroes, id=hero2_id))
    print(list_pair)

    # attacker = []
    # defender = []
    # hp1 = list_pair[0].hero_stamina * 40
    # hp2 = list_pair[1].hero_stamina * 40
    # while hp1 > 0 and hp2 > 0:
    #     defender, attacker = r.sample(list_pair, 2)
    #     defender
    #     hit_points = defender.hp
    #     defender.defence_damaged(attacker.base_attack,
    #                              defender.base_defence)









    return render(request, 'arena.html', {'person_list': list_pair})

