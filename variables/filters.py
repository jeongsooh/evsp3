import django_filters
from .models import Variables

class VariablesFilter(django_filters.FilterSet):
  class Meta:
    model = Variables
    fields = {
      'variable':['exact'],
      'group':['exact'],
      'value':['exact'],
    }