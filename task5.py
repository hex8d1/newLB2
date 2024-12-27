from flask import Flask, request
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

NBU_API_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&date={}&json"

def get_exchange_rate(date):
    response = requests.get(NBU_API_URL.format(date))
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['rate']
    return None

@app.route('/currency', methods=['GET'])
def currency():
    param = request.args.get('param')
    if param == 'today':
        today_date = datetime.now().strftime('%Y%m%d')
        rate = get_exchange_rate(today_date)
        if rate:
            return f"Курс USD на сегодня: {rate}"
        else:
            return "Ошибка получения курса валют", 500
    elif param == 'yesterday':
        yesterday_date = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d')
        rate = get_exchange_rate(yesterday_date)
        if rate:
            return f"Курс USD на вчера: {rate}"
        else:
            return "Ошибка получения курса валют", 500
    else:
        return "Неверный параметр. Используйте 'today' или 'yesterday'.", 400

if __name__ == "__main__":
    app.run(port=8000)
