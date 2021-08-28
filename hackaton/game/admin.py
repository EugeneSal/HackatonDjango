from django.contrib import admin


from .models import *


class PaladinAdmin(admin.ModelAdmin):
    list_display = ('name_class', 'name', 'nick_name',
                    'hero_strength', 'hero_stamina', 'hero_armor',
                    'default_strength', 'default_stamina', 'default_armor')
    search_fields = ('name',)
    list_filter = ('name_class',)
    # list_select_related = ('name', 'nick_name')
    empty_value_display = '-пусто-'


class DruidAdmin(admin.ModelAdmin):
    list_display = ('name_class', 'name', 'nick_name',
                    'hero_strength', 'hero_stamina', 'hero_armor',
                    'default_strength', 'default_stamina', 'default_armor')
    search_fields = ('name',)
    list_filter = ('name_class',)
    # list_select_related = ('name', 'nick_name')
    empty_value_display = '-пусто-'


class WarriorAdmin(admin.ModelAdmin):
    list_display = ('name_class', 'name', 'nick_name',
                    'hero_strength', 'hero_stamina', 'hero_armor',
                    'default_strength', 'default_stamina', 'default_armor')
    search_fields = ('name',)
    list_filter = ('name_class',)
    # list_select_related = ('name', 'nick_name')
    empty_value_display = '-пусто-'


class ThingsAdmin(admin.ModelAdmin):
    list_display = ('name_class', 'name', 'owners',
                    'thing_strength', 'thing_stamina', 'thing_armor')
    search_fields = ('name',)
    list_filter = ('name_class', 'name')
    # list_select_related = ('name', 'nick_name')
    empty_value_display = '-пусто-'


admin.site.register(Warrior, WarriorAdmin)
admin.site.register(Paladin, PaladinAdmin)
admin.site.register(Druid, DruidAdmin)
admin.site.register(Things, ThingsAdmin)
