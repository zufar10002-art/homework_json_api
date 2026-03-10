\# Проект конвертации валют



\## Описание

Проект для работы с банковскими транзакциями из JSON-файла и конвертации валют (USD, EUR) в рубли через внешнее API.



\## Функциональность

\- Чтение данных о транзакциях из JSON-файла

\- Конвертация сумм из USD и EUR в рубли по актуальному курсу

\- Обработка ошибок (файл не найден, пустой файл, проблемы с API)

\- Сокрытие чувствительных данных (API ключ) в переменных окружения



\## Установка

1\. Клонировать репозиторий

2\. Создать виртуальное окружение: `python -m venv venv`

3\. Активировать: `venv\\Scripts\\activate` (Windows)

4\. Установить зависимости: `pip install -r requirements.txt`

5\. Создать файл `.env` и добавить API ключ: `EXCHANGE\_API\_KEY=ваш\_ключ`



\## Использование

```python

from src.utils import load\_operations

from src.external\_api import convert\_to\_ruble



\# Загрузка транзакций

operations = load\_operations("data/operations.json")



\# Конвертация первой транзакции в USD

if operations and operations\[0]\['operationAmount']\['currency']\['code'] == 'USD':

&nbsp;   rubles = convert\_to\_ruble(operations\[0])

&nbsp;   print(f"Сумма в рублях: {rubles}")

