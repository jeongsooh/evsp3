from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from django.db.models import Q

from .models import Cpinfo

# Create your views here.

class CpinfoList(ListView):
  model = Cpinfo
  template_name='cpinfo.html'
  context_object_name = 'cpinfoList'
  paginate_by = 2
  queryset = Cpinfo.objects.all()

  def get_queryset(self):
    queryset = Cpinfo.objects.all()
    query = self.request.GET.get("q", None)
    if query is not None:
      queryset = queryset.filter(
        Q(cpstatus__icontains=query) |
        Q(cpnumber__icontains=query) |
        Q(cpsite__icontains=query) |
        Q(register_dttm__icontains=query)
      )
    return queryset
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_id = self.request.session['user']
    context['loginuser'] = user_id

    return context
  
class CpinfoCreateView(CreateView):
  model = Cpinfo
  template_name = 'cpinfo_register.html'
  fields = ['cpnumber', 'cpsite', 'address', 'partner_id', 'manager_id', 'public_use', 'fwversion','cpstatus', 'cpmodel', 'cpmaker']
  success_url = '/cpinfo'

class CpinfoDeleteView(DeleteView):
    model = Cpinfo
    template_name='cpinfo_confirm_delete.html'
    success_url = '/cpinfo'