from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator

# from rest_framework import generics
# from rest_framework import mixins
from .models import Charginginfo
from .filters import CharginginfoFilter
# from .serializers import CharginginfoSerializer

# Create your views here.

class CharginginfoList(ListView):
  model = Charginginfo
  template_name='charginginfo.html'
  context_object_name = 'charginginfoList'
  paginate_by = 3
  queryset = Charginginfo.objects.all()

  def get_queryset(self):
    queryset = Charginginfo.objects.all()
    self.filterset = CharginginfoFilter(self.request.GET, queryset=queryset)
    return self.filterset.qs

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_id = self.request.session['user']
    context['loginuser'] = user_id
    context['form'] = self.filterset.form
    return context
  
class CharginginfoCreateView(CreateView):
  model = Charginginfo
  template_name = 'charginginfo_register.html'
  fields = ['cpnumber', 'userid', 'energy', 'amount', 'start_dttm', 'end_dttm',]
  success_url = '/charginginfo'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_id = self.request.session['user']
    context['loginuser'] = user_id
    print(context['form'])
    
    return context