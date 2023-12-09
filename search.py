import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Уровни доступа, которые наше приложение запрашивает.
# Если нужны какие-то другие, необходимо удалить файл token.json
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# Идентификатор таблицы и диапазон поиска
SAMPLE_SPREADSHEET_ID = "1wYvGoWYuiaWkIC05484NKLoNIDgXX-ENf0jGHaCM-3Y"
SAMPLE_RANGE_NAME = "A2:A"

def authorize():
  creds = None
  # Файл token.json хранит токены доступа конкретного пользователя, этот файл
  # создаётся автоматически при первом запуске в случае успешной авторизации
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # Если файла с ключами доступа нет, запрашиваем авторизацию
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Сохраняем токены в файл, чтобы повторно не спрашивать
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  return creds


def search_in_spreadsheet(number):
  # return {
  #   "id": int(number),
  #   "name": "Батончик",
  #   "shops": [
  #     { "name": "Аникс", "price": 88.30 },
  #     { "name": "Мария", "price": 45.34 }
  #   ]
  # }

  creds = authorize()

  try:
    # Инициализируем клиент для доступа к API
    service = build("sheets", "v4", credentials=creds)

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
