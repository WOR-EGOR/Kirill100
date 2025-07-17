def filter_by_state(dicta, state="EXECUTED"):
    """Функция фильтрует слово по умолчанию, и формирует список"""
    new_dict = []
    for value in dicta:
        if value.get("state") == state:
            new_dict.append(value)
    return new_dict


def sort_by_date(dicta, sta=True):
    """сортирует словарь по убыванию"""
    return sorted(dicta, key=lambda item: item["date"], reverse=True)
