import os

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Уровни доступа, которые наше приложение запрашивает
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# Идентификатор таблицы и диапазон поиска
SAMPLE_SPREADSHEET_ID = "1wYvGoWYuiaWkIC05484NKLoNIDgXX-ENf0jGHaCM-3Y"
SAMPLE_RANGE_NAME = "A2:A"

def search_in_spreadsheet(number):
  # return {
  #   "id": int(number),
  #   "name": "Батончик",
  #   "shops": [
  #     { "name": "Аникс", "price": 88.30 },
  #     { "name": "Мария", "price": 45.34 }
  #   ]
  # }

  os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'

  try:
    # Инициализируем клиент для доступа к API
    service = build("sheets", "v4")

    # Отправляем запрос к Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )

    # Результат запроса: массив строк из таблицы
    values = result.get("values", [])

    if not values:
      print("Ничего не найдено в таблице.")
      return

    for row in values:
      # print(row[0])
      # print(number)

      if row[0] == number:
        print('Совпадение!')

  except HttpError as err:
    print(err)
