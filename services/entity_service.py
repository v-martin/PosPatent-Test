from django.db.models import Model
from api.models import Entity


def get_entity_by_attrs(**attrs) -> list[Model]:
    print(attrs)
    query_attrs = {key: _get_attr(value) for key, value in attrs.items()
                   if value != '' and key != 'csrfmiddlewaretoken'}
    patents = Entity.objects.filter(**query_attrs).all()
    return list(patents)


def get_entity_context(entities: list[Model]) -> list[dict]:
    contexts = []
    for entity in entities:
        fields = entity._meta.get_fields()
        context = {f"{str(field).split('.')[- 1]}": entity.__dict__[field.name] for field in fields}
        contexts.append(context)
    return contexts


def _get_attr(attr: str):
    if attr in 'offon':
        return True if attr == 'on' else False
    elif attr == '':
        return None
    else:
        try:
            return int(attr)
        except ValueError:
            return attr


def _get_table(num: int) -> type[Model] | None:
    tables = {0: Patent}
    return tables.get(num)
