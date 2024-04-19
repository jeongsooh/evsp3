from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
# from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime, timezone, timedelta
from dateutil.relativedelta import relativedelta
from cpinfo.models import Cpinfo
from user.models import User
from charginginfo.models import Charginginfo

from user.forms import LoginForm
from django.db.models import Q
# from .forms import Cpinfo RegisterForm

# Create your views here.

@csrf_exempt
def index(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      request.session['user'] = form.data.get('userid')
      return redirect('/dashboard')
  else:
    form = LoginForm()
  return render(request, 'index.html', {'form': form})

def logout(request):
  if 'user' in request.session:
    del(request.session['user'])

  return redirect('/')

def dashboard(request):
  dt_now = datetime.now()
  thismonth = str(dt_now)[:7]
  lastmonth = str(dt_now - relativedelta(months=1))[:7]

  queryset = Cpinfo.objects.all()
  total_cp = queryset.count()
  cp_lastmonth = queryset.filter(Q(register_dttm__icontains=lastmonth)).count()
  cp_thismonth = queryset.filter(Q(register_dttm__icontains=thismonth)).count()

  queryset = User.objects.all()
  total_user = queryset.count()
  user_lastmonth = queryset.filter(Q(register_dttm__icontains=lastmonth)).count()
  user_thismonth = queryset.filter(Q(register_dttm__icontains=thismonth)).count()

  queryset = Charginginfo.objects.all().values()
  total_charging = sum([item['energy'] for item in queryset]) / 1000
  charging_lastmonth = sum([item['energy'] for item in queryset.filter(Q(end_dttm__icontains=lastmonth))]) / 1000
  charging_thismonth = sum([item['energy'] for item in queryset.filter(Q(end_dttm__icontains=thismonth))]) / 1000
  rev_lastmonth = sum([item['amount'] for item in queryset.filter(Q(end_dttm__icontains=lastmonth))])
  rev_thismonth = sum([item['amount'] for item in queryset.filter(Q(end_dttm__icontains=thismonth))])

  user_id = request.session['user']
  return render(request, 'dashboard.html', {'loginuser': user_id,
    'total_cp': total_cp, 'cp_lastmonth': cp_lastmonth, 'cp_thismonth': cp_thismonth,
    'total_user': total_user, 'user_lastmonth': user_lastmonth, 'user_thismonth': user_thismonth,
    'total_charging': total_charging, 'charging_lastmonth': charging_lastmonth, 'charging_thismonth': charging_thismonth,
    'rev_lastmonth': rev_lastmonth, 'rev_thismonth': rev_thismonth
    })
