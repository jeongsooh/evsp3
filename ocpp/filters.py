import django_filters
from .models import Ocpp

class OcppFilter(django_filters.FilterSet):
  # cpnumber = django_filters.CharFilter(lookup_expr='iexact')
  # msg_name = django_filters.CharFilter(lookup_expr='iexact')
  # register_dttm = django_filters.NumberFilter(field_name='register_dttm', lookup_expr='date')
  # register_dttm__gte = django_filters.NumberFilter(field_name='register_dttm', lookup_expr='date__gte')
  # register_dttm__lte = django_filters.NumberFilter(field_name='register_dttm', lookup_expr='date__lte')
  class Meta:
    model = Ocpp
    # fields = ['cpnumber', 'msg_name', 'register_dttm']
    fields = {
      'cpnumber':['exact'],
      'msg_name':['exact'],
      'register_dttm':['gte', 'lte'],
    }