def compute_stock_totals():

    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }
    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }

    #  порожній словник для результатів
    totals = {}

    # пройти циклом for по ключах словника stock
    for item in stock:
     # назва товару (item) в обох словниках, вартість= кількість * ціна
        total_item_price = stock[item] * prices[item]

        #  результат в новому словнику
        totals[item] = total_item_price

    return totals

if __name__ == "__main__":
    result = compute_stock_totals()
    print("Вартість запасів за типами товарів:")
    print(result)

    # загальна сума всього складу
    total_sum = sum(result.values())
    print(f"\nЗагальна сума всього складу: {total_sum}")