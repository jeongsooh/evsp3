# management/commands/delete_obj.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from clients.models import Clients

class Command(BaseCommand):
    help = 'Deletes all objects by model name or date range'

    def add_arguments(self, parser):
        parser.add_argument('--model', type=str, help='Model objects to delete')
        parser.add_argument('--from', type=str, help='Start date of the range')
        parser.add_argument('--to', type=str, help='End date of the range')

    def handle(self, *args, **options):
        model = options['model']
        from_date = options['from']
        to_date = options['to']
        if model == 'Clients':
            queryset = Clients.objects.all()
            queryset.delete()
            self.stdout.write(f'Deleted objects in Model {queryset.count()}')
        elif from_date and to_date:
            objs = MyModel.objects.filter(date__range=[from_date, to_date])
            objs.delete()
            self.stdout.write(f'Deleted objects from {from_date} to {to_date}')
        else:
            self.stdout.write(f'Invalid arguments: {model}')
