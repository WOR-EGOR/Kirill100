def filter_by_state(privet, state="EXECUTED"):
    """Функция фильтрует слово по умолчанию, и формирует список"""
    new_dict = []
    for value in privet:
        if value.get("state") == state:
            new_dict.append(value)
    return new_dict


def sort_by_date(privet, sta=True):
    """сортирует словарь по убыванию"""
    return sorted(privet, key=lambda item: item["date"], reverse=True)
