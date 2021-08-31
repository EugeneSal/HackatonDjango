# HackatonDjango
### Мини игра (альфа-версия MVP)
***
### Возможности:
* создание персонажей 3 классов Воин, Паладин, Друид
* создание предметов для персонажей
* одевание персонажей предметами
* выбор пары для сражения
***
### Как запустить проект:
```
https://github.com/EugeneSal/HackatonDjango.git
```
Создать и активировать виртуальное окружение:
```
python -m venv env

source venv/bin/activate
```
Обновить pip
```
python -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python manage.py migrate
```
Запустить сервер:
```
python manage.py runserver
```
Ссылка на локальный сервер:
http://127.0.0.1:8000/
