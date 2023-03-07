import requests
import json
import time

# URL для получения цены ETHUSDT
url = "https://fapi.binance.com/fapi/v1/ticker/price?symbol=ETHUSDT"

# Устанавливаем интервал обновления цены в секундах
interval = 1

# Процент изменения цены для вывода сообщения
change_percent = 1

# Время в минутах, за которое мы будем отслеживать изменение цены
time_window = 60


# Функция для получения текущей цены ETHUSDT
def get_price():
    response = requests.get(url)
    data = json.loads(response.text)
    return float(data["price"])


# Функция для вычисления процентного изменения цены
def get_price_change_pct(price1, price2):
    return abs(price1 - price2) / price1 * 100


# Определяем начальную цену и время запуска
prev_price = get_price()
start_time = time.time()

print("Программа запущена. Ожидание изменения цены...")

while True:
    # Периодически запрашиваем текущую цену и вычисляем изменение
    curr_price = get_price()
    price_change_pct = get_price_change_pct(curr_price, prev_price)

    # Если процент изменения цены больше указанного значения и цена изменялась в течение последних time_window минут
    if price_change_pct >= change_percent and time.time() - start_time <= time_window * 60:
        print(f"Изменение цены: {price_change_pct:.2f}% за последние {time_window} минут.")

    prev_price = curr_price
    time.sleep(interval)
