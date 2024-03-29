# myapp/management/commands/runserver.py
from django.core.management.commands.runserver import Command as RunserverCommand
from django.core.management import call_command

class Command(RunserverCommand):
    def inner_run(self, *args, **options):
        # call delete_obj command before runserver
        call_command('delete_obj', '--model', 'Clients')
        # call original runserver command
        super(Command, self).inner_run(*args, **options)
