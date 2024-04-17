from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView

from .models import Ocpp
from .filters import OcppFilter
# from .forms import MessageForm

# Create your views here.

class OcppList(ListView):
  model = Ocpp
  template_name='ocpp.html'
  context_object_name = 'ocppList'
  paginate_by = 20
  queryset = Ocpp.objects.all()

  def get_queryset(self):
    queryset = Ocpp.objects.all()
    self.filterset = OcppFilter(self.request.GET, queryset=queryset)
    return self.filterset.qs

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_id = self.request.session['user']
    context['loginuser'] = user_id
    context['form'] = self.filterset.form
    return context
  
class OcppDeleteAllView(DeleteView):
    model = Ocpp
    template_name='ocpp_confirm_delete.html'
    success_url = '/ocpp'

def ocppdeleteall(request):
  # ocppList = request.GET.get('target')

  if request.method == 'POST':
    print('POST requested')
  else:
    print('GET requested')
  return redirect('/ocpp')
