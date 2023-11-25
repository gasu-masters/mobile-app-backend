from flask import abort, Flask, render_template, request
from . import search

# Инициализация приложения
app = Flask(__name__)

# Добавляем стартовую страницу в наше приложение
# Страница содержит веб-форму, поэтому должна понимать запросы GET и POST
@app.route("/", methods=('GET', 'POST'))
def index():
    result = []

    # Выводим введённый пользователем номер в консоль
    if request.method == 'POST':
        number = request.form['number']

        if number is None or number == '':
            abort(400)

        number = float(number)

        # Запрашиваем актуальные курсы валют
        try:
            result = search.search_in_spreadsheet(number)
        except:
            abort(500)

    # Передаём результаты поиска в нашу программу
    return render_template('index.html', result=result)

@app.errorhandler(500)
def error_connecting_to_rates(e):
    return render_template('500.html'), 500

@app.errorhandler(400)
def no_number_provided(e):
    return render_template('400.html'), 400
