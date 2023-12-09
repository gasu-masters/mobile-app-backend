BASE_URI = 'https://docs.google.com/spreadsheets/d/'
SHEET_ID = '1wYvGoWYuiaWkIC05484NKLoNIDgXX-ENf0jGHaCM-3Y'

def search_in_spreadsheet(number):
  return {
    "id": int(number),
    "name": "Батончик",
    "shops": [
      { "name": "Аникс", "price": 88.30 },
      { "name": "Мария", "price": 45.34 }
    ]
  }