import csv
from django.core.management import BaseCommand
from loguru import logger
from api.models import Entity


def _decimal_to_float(dec: str) -> float:
    if '/' in dec:
        num, denom = map(int, dec.split('/'))
        return float(num / denom)
    else:
        return float(dec)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)
        parser.add_argument('table', type=str)

    def handle(self, *args, **options):
        with open(options['filename'], encoding='utf-8') as f:
            reader = csv.reader(f)
            count = 0
            columns = next(reader)
            columns = list(map(lambda x: x.replace('\ufeff', ''), columns))
            fields = ['registration number', 'registration date', 'application number', 'application date',
                      'actual', 'publication URL']
            tables = ['Inventions', 'GeographicNames', 'UsefulModels', 'IndustrialDesigns', 'Trademarks',
                      'WellknownTrademarks', 'Databases', 'MainframeSoftware', 'TopologyOfIntegratedCircuits']
            indexes = [index for index, value in enumerate(columns) if value in fields]
            while count < 500:
                row = next(reader)
                count += 1
                patent, is_created = Entity.objects.get_or_create(
                    registration_number=row[indexes[0]].replace('\ufeff', '')
                    if row[indexes[0]] else None,
                    registration_date=int(row[indexes[1]]) if row[indexes[1]] else None,
                    application_number=int(row[indexes[2]]) if row[indexes[2]] else None,
                    application_date=int(row[indexes[3]]) if row[indexes[3]] else None,
                    actual=bool(row[indexes[4]]) if row[indexes[4]] else None,
                    publication_url=row[indexes[5]] if row[indexes[5]] else None,
                    table=options['table'] if options['table'] in tables else None
                )
                if is_created:
                    logger.debug(f'Entity {patent.registration_number} created!')
                else:
                    logger.debug(f'Entity {patent.registration_number} already exists!')
