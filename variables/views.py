from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from django.db.models import Q

from .models import Variables
from .filters import VariablesFilter

# Create your views here.

class VariablesList(ListView):
  model = Variables
  template_name='variables.html'
  context_object_name = 'variablesList'
  paginate_by = 10
  queryset = Variables.objects.all()

  def get_queryset(self):
    queryset = Variables.objects.all()
    query = self.request.GET.get("q", None)
    if query is not None:
      queryset = queryset.filter(
        Q(variable__icontains=query) |
        Q(value__icontains=query)
      )
    return queryset

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_id = self.request.session['user']
    context['loginuser'] = user_id
    return context

class VariablesDetail(DetailView):
  template_name='variables_detail.html'
  queryset = Variables.objects.all()
  context_object_name = 'variables'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_id = self.request.session['user']
    context['loginuser'] = user_id
    
    return context

class VariablesUpdateView(UpdateView):
  model = Variables
  template_name='variables_update.html'
  fields = ['variable', 'group', 'value']
  success_url = '/variables'

class VariablesCreateView(CreateView):
  model = Variables
  template_name = 'variables_register.html'
  fields = ['variable', 'group', 'value']
  success_url = '/variables'

class VariablesDeleteView(DeleteView):
    model = Variables
    template_name='variables_confirm_delete.html'
    success_url = '/variables'