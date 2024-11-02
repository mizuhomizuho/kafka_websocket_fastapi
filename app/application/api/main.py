from fastapi import FastAPI


def create_app():
    return FastAPI(
        title='Kafka WebSocket API ddd',
        docs_url='/api/docs',
        description='Meow',
        debug=True,
    )


r'''

Посмотреть dataclasses + dataclass + field, property, мутабельные типы

Гарантии доставки:
at least once - хотя бы один раз (Идемпотентность данных — это свойство некоторых операций, при котором повторное выполнение операции не приводит к изменению состояния системы или ресурса.)
at most once - самое большее один раз
exactly-once - ровно 1 раз (сложнее в распределенных системах)

Сообщения попадают в 1 партишн если имеют 1 ключ, тогда сообщения идут последовательно, иначе параллельно

pip install poetry
poetry init
poetry add fastapi motor uvicorn ipython pytest
poetry remove faker

https://github.com/greedWizard/django-docker-compose-postgres-boilerplate
https://github.com/greedWizard/ddd-fastapi-kafka-chat

entities (domain) -> repositories (infra) -> services (logic) -> entrypoints (application)

& "C:\Program Files (x86)\GnuWin32\bin\make.exe" app
'''