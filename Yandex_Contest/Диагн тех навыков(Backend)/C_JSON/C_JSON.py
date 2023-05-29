"""C. Опять JSON’ы перекладывать...
Ограничение времени	2 секунды
Ограничение памяти	256.0 Мб
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Всем хотя бы раз в жизни приходилось перекладывать JSON. Вот и для нового проекта под названием "Единое хранилище" необходимо переложить магазинные фиды. Для размещения на Яндекс.Маркете магазины передают товары из своего ассортимент в JSON-файлах. Одно товарное предложение описывается так:
{
    "offer_id": <string>,
    "market_sku": <int>,
    "price": <int>
}
где
offer_id - уникальный среди всех фидов магазина идентификатор предложения,
market_sku - идентификатор товара на Яндекс.Маркете,
price - стоимость товара.

Весь фид магазина представляет собой JSON и выглядит так:
{
    "offers": [<offer>, <offer>, ...]
}
Вас попросили написать программу, которая объединит все фиды одного магазина в единый фид и отсортирует товары в порядке неубывания их стоимостей, а при их равенстве - по
offer_id.

Формат ввода
В первой строке входных данных содержится целое число
n - количество фидов магазина (1≤n≤200). Следующие
n строк содержат по одному магазинному фиду на строку. Гарантируется, что строка - валидный JSON и удовлетворяет формату фида. В одном фиде не больше 200 товарных предложений.
offer_id состоит из строчных и заглавных букв латинского алфавита и цифр,
1≤∣offer_id∣≤10,
1≤market_sku≤2**31−1,
1≤price≤10.

Формат вывода
Выходной поток должен содержать один JSON-документ, удовлетворяющий формату товарного фида. Количество строк в выходном файле и табуляция не имеют значения.

Пример
Ввод
2
{"offers": [{"offer_id": "offer1", "market_sku": 10846332, "price": 1490}, {"offer_id": "offer2", "market_sku": 682644, "price": 499}]}
{"offers": [{"offer_id": "offer3", "market_sku": 832784, "price": 14000}]}
Вывод
{"offers":[{"market_sku":682644,"offer_id":"offer2","price":499},{"market_sku":10846332,"offer_id":"offer1","price":1490},{"market_sku":832784,"offer_id":"offer3","price":14000}]}
Примечания
Для решений на языке python доступны все стандартные библиотеки, включая json."""
import json
from typing import Dict


def input_data() -> Dict:
    key = "offers"
    data = dict()
    data[key] = []
    n = int(input().strip())
    for _ in range(n):
        read_line = json.loads(input().strip())
        for i in range(len(read_line[key])):
            line_dict = dict(sorted(read_line[key][i].items(),
                                    key=lambda item: item[0]))
            data.get(key).append(line_dict)
    return data


def sorting_data(data: Dict) -> Dict:
    sorted_data = dict()
    sorted_data["offers"] = sorted(data.get('offers'),
                                   key=lambda item: (dict(item)['price'],
                                                     dict(item)['offer_id']))
    return sorted_data


def save_jsonfile(data:Dict):
    with open("output.txt", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)



if __name__ == '__main__':
    data = input_data()
    sorted_data = sorting_data(data)
    print(sorted_data)
    # save_jsonfile(sorted_data)
