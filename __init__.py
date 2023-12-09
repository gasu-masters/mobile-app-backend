from flask import abort, Flask, render_template, request
from . import search

# Инициализация приложения
app = Flask(__name__)

# Добавляем стартовую страницу в наше приложение
# Страница содержит веб-форму, поэтому должна понимать запросы GET и POST
@app.route("/", methods=('GET', 'POST'))
def index():
    result = []

    if request.method == 'POST':
        number = request.form['number']
        # Выводим введённый пользователем номер в консоль
        print(number)

        if number is None or number == '':
            abort(400)

        # Ищем номер в таблице
        try:
            result = search.search_in_spreadsheet(number)
        except:
            abort(500)

    # Выводим результаты поиска на экран
    return render_template('index.html', result=result)

@app.errorhandler(500)
def error_connecting_to_rates(e):
    return render_template('500.html'), 500

@app.errorhandler(400)
def no_number_provided(e):
    return render_template('400.html'), 400
