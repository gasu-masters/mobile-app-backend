from flask import abort, Flask, render_template, request
from . import search

# Инициализация приложения
app = Flask(__name__)

# Добавляем стартовую страницу в наше приложение
@app.route("/", methods=(['GET']))
@app.route("/<number>", methods=(['GET']))
def index(number = None):
    result = []

    if number is None or number == '':
        abort(400)

    # Ищем номер в таблице
    try:
        result = search.search_in_spreadsheet(number)
        print(result)

        if result is None:
            abort(404)
    except:
        abort(500)

    return result

@app.errorhandler(500)
def error_connecting_to_rates(e):
    response = {"error": "Не получилось выполнить запрос к API"}
    return response, 500

@app.errorhandler(400)
def no_number_provided(e):
    response = {"error": "Плохой запрос, необходим набор цифр"}
    return response, 400

@app.errorhandler(404)
def not_found(e):
    response = {"error": "Ничего не найдено"}
    return response, 404
