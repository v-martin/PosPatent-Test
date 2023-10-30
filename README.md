# РосПатентПоиск

## Описание

Сервис, реализовывающий поиск по базам данных с [сайта РосПатента](https://rospatent.gov.ru/opendata).
Таблицы загружены в удаленный сервер Railway(PostgreSQL) кастомными консольными командами Django.

## Запуск
Должен быть установлен Python(желательно 3.10 версии)

`git pull https://github.com/v-martin/PosPatent-Test.git`

`pip install -r requirments.txt`

`python manage.py runserver`
