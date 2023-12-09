# Функционал

- получить GET-запрос с ID, соответствующим штрих-коду в формате EAN-13, вида http://127.0.0.1/4601234567890
- отправить запрос к API электронной таблицы и найти строку, соответствующую штрих-коду
- вернуть результат в формате JSON

# Установка

Зависимости: Python, Flask

1. Устанавливаем Python по инструкции с официального сайта https://www.python.org
2. Устанавливаем [Flask](https://flask.palletsprojects.com/) через `pip`:

```
python -m pip install flask
```

3. Устанавливаем гугловские зависимости через `pip`:

```
python3 -m pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```


# Запуск

Находясь в директории проекта выполнить (использование `.` после `--app` означает текущую папку):

```
python -m flask --app . run --debug 
```