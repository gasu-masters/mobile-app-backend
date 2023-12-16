import os

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Уровни доступа, которые наше приложение запрашивает
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# Идентификатор таблицы и диапазон поиска
SAMPLE_SPREADSHEET_ID = "1wYvGoWYuiaWkIC05484NKLoNIDgXX-ENf0jGHaCM-3Y"
SAMPLE_RANGE_NAME = "A2:G"
SHOP_NAMES_RANGE="C1:G1"

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
    found_row = None

    # Результат запроса: массив строк из таблицы
    values = result.get("values", [])

    if not values:
      print("Ничего не найдено в таблице.")
      return

    for row in values:
      if row[0] == number:
        print(row)
        found_row = {
          "id": int(number),
          "name": row[1],
          "shops": [
            { "name": "Магнит", "price": float(row[2]) },
            { "name": "Пятерочка", "price": float(row[3]) },
            { "name": "Аникс", "price": float(row[4]) },
            { "name": "Мария-РА", "price": float(row[5]) },
            { "name": "Fix Price", "price": float(row[6]) }
          ]
        }

    return found_row

  except HttpError as err:
    print(err)
