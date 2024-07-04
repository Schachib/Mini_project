from decimal import Decimal
from datetime import datetime, date, timedelta

DATE_FORMAT = '%Y-%m-%d'
goods = {
    'Пельмени Универсальные':
        [
            {
                'amount': Decimal('0.5'), 'expiration_date': datetime.strptime('2024-7-15', DATE_FORMAT).date()
            },
            {
                'amount': Decimal('2'), 'expiration_date': datetime.strptime('2024-8-1', DATE_FORMAT).date()
            },
        ],
    'Вода':
        [
            {
                'amount': Decimal('1.5'), 'expiration_date': None
            }
        ]
}


def add(items, title, amount, expiration_date=None):
    expiration_date = datetime.strptime(expiration_date, DATE_FORMAT).date() if expiration_date else expiration_date
    if title in items:
        items[title].append({'amount': amount, 'expiration_date': expiration_date})
    else:
        items[title] = [{'amount': amount, 'expiration_date': expiration_date}]


def add_by_note(items, note):
    #  Добавление продукта
    hare_str = note.split(' ')  # [ 'Яйца', 'Фабрики', '№1', '4', '2024-07-15']
    expiration_date = hare_str[-1] if len(hare_str[-1].split('-')) == 3 else None
    check_amount = Decimal(hare_str[-2] if expiration_date else hare_str[-1])
    product_name = ' '.join(hare_str[:-2] if expiration_date else hare_str[:-1])
    add(items, product_name, check_amount, expiration_date)


def find(items, needle):
    #  Поиск продукта по его приблизитульному описанию
    result_list = []
    for title in items:
        lower_title = title.lower()
        if needle.lower() in lower_title:
            result_list.append(title)
    return result_list
    # Укороченный вариант
    # return [title for title in items if needle.lower() in title.lower()]

def amount(items, needle):
    # Подсчёт продукта после поиска на навзанию
    title_list = find(items, needle)  # Тут могла быть ваша реклама
    sum_amout = Decimal(0)
    for key, value in items.items():
        if key in title_list:
            for item in value:
                sum_amout += item['amount']
    return Decimal(sum_amout)
    # Укороченный вариант
    # return sum(item['amount'] for title, value in items.items() for item in value if title in title_list)

def expire(items, in_advance_days=0):
    # Проверка срока годности товара по дате
    date_now = date_now = datetime.today().date() + timedelta(days=in_advance_days)
    expired_products = []

    for key, value in items.items():
        total_amount = 0
        for item in value:
            if item['expiration_date'] and date_now >= item['expiration_date']:
                total_amount += Decimal(item['amount'])
        if total_amount > 0:
            expired_products.append((key, total_amount))
    return expired_products
    # Укороченный вариант
    #date_now = datetime.today().date() + timedelta(days=in_advance_days)
    #    expired_products = [
    #        (key, sum(item['amount'] for item in value if item['expiration_date'] and date_now >= item['expiration_date']))
    #        for key, value in items.items() if
    #        sum(item['amount'] for item in value if item['expiration_date' and date_now >= item['expiration_date']) > 0]


add(goods, 'Сок', 5, '2024-07-1')
add(goods, 'Сок', 10)

add_by_note(goods, 'Фабрик №1 4 2024-07-1')
add_by_note(goods, 'Фабрик №1 5 2024-07-1')
add_by_note(goods, 'Фабрик №3 5')
'''print(find(goods, 'фа'))
print(amount(goods, 'фАБРИК'))'''
print(expire(goods, 0))
