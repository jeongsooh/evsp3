from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.views.generic.edit import FormView

from django.db.models import Q

from .models import Clients
from .forms import (ClientsResetForm, ChargingProfileForm, CompositeScheduleForm, 
      ClearChargingProfileForm, RemoteStartForm, RemoteStopForm, ClientsClearcacheForm,
      ClientsUnlockConnForm, ClientsGetconfForm, ClientsSetconfForm, ClientsGetLocalListForm,
      ClientsSendLocalListForm, ClientsUpdateFirmwareForm, ClientsGetDiagForm, ClientsReserveNowForm,
      ClientsChangeAvailableForm, ClientsCancelReservationForm, ClientsTriggerMessageForm,
      DataTransferForm)

from ocpp.client_gateway import ( reset_cpinfo, update_cpinfo, clearcache_cpinfo, 
      remotestart_cpinfo, remotestop_cpinfo, unlock_connector, get_conf, set_conf,
      set_charging_profile, clear_charging_profile, get_composite_schedule, get_locallist,
      send_locallist, update_firmware, get_diagnostics, reserve_now, change_available, cancel_reservation,
      trigger_message, data_transfer)

# Create your views here.

class ClientsList(ListView):
  model = Clients
  template_name='clients.html'
  context_object_name = 'clientsList'
  paginate_by = 5
  queryset = Clients.objects.all()

  def get_queryset(self):
    queryset = Clients.objects.all()
    query = self.request.GET.get("q", None)
    if query is not None:
      queryset = queryset.filter(
        Q(cpnumber__icontains=query) |
        Q(cpstatus__icontains=query) |
        Q(channel_status_1__icontains=query)
      )
    return queryset

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_id = self.request.session['user']
    context['loginuser'] = user_id
    return context

class ClientsDeleteView(DeleteView):
    model = Clients
    template_name='clients_confirm_delete.html'
    success_url = '/clients'

class ClientsDetail(DetailView):
  template_name='clients_detail.html'
  queryset = Clients.objects.all()
  context_object_name = 'clients'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_id = self.request.session['user']
    context['loginuser'] = user_id
    
    return context

class ClientsClearcacheView(FormView):
  template_name = 'clients_clearcache.html'
  form_class = ClientsClearcacheForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    clearcache_cpinfo(cpnumber)

    return super().form_valid(form) 

class RemoStartChargeView(FormView):
  template_name = 'clients_remostart.html'
  form_class = RemoteStartForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    id_tag = form.data.get('id_tag')

    charging_schedule_period = []
    start_period1 = form.data.get('start_period1')
    period_limit1 = form.data.get('period_limit1')
    if  start_period1 and period_limit1:
      charging_schedule_period.append({'startPeriod': int(start_period1), 'limit': int(period_limit1)})
    start_period2 = form.data.get('start_period2')
    period_limit2 = form.data.get('period_limit2')
    if  start_period1 and period_limit1:
      charging_schedule_period.append({'startPeriod': int(start_period2), 'limit': int(period_limit2)})
    start_period3 = form.data.get('start_period3')
    period_limit3 = form.data.get('period_limit3')
    if  start_period3 and period_limit3:
      charging_schedule_period.append({'startPeriod': int(start_period3), 'limit': int(period_limit3)})
    start_period4 = form.data.get('start_period4')
    period_limit4 = form.data.get('period_limit4')
    if  start_period4 and period_limit4:
      charging_schedule_period.append({'startPeriod': int(start_period4), 'limit': int(period_limit4)})

    charging_profile = {
      'charging_profile_id' : form.data.get('charging_profile_id'),
      'charging_profile_level' : form.data.get('charging_profile_level'),
      'charging_profile_purpose' : form.data.get('charging_profile_purpose'),
      'charging_profile_kind' : form.data.get('charging_profile_kind'),
      'charging_schedule_period' : charging_schedule_period
    }

    remotestart_cpinfo(cpnumber, id_tag, charging_profile)

    return super().form_valid(form) 

class RemoStopChargeView(FormView):
  template_name = 'clients_remostop.html'
  form_class = RemoteStopForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    transaction_id = int(form.data.get('transaction_id'))
    remotestop_cpinfo(cpnumber, transaction_id)

    return super().form_valid(form) 

class UnlockConnView(FormView):
  template_name = 'clients_unlockconn.html'
  form_class = ClientsUnlockConnForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    connector_id = int(form.data.get('connector_id'))
    unlock_connector(cpnumber, connector_id)

    return super().form_valid(form) 

class GetConfView(FormView):
  template_name = 'clients_getconf.html'
  form_class = ClientsGetconfForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    keys = form.data.get('keys')
    if keys:
      get_conf(cpnumber, eval(keys))
    else:
      get_conf(cpnumber, keys)

    return super().form_valid(form) 

class SetConfView(FormView):
  template_name = 'clients_setconf.html'
  form_class = ClientsSetconfForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    keys = form.data.get('keys')
    set_conf(cpnumber, eval(keys))

    return super().form_valid(form) 

class GetLocalListVersionView(FormView):
  template_name = 'clients_getlocallist.html'
  form_class = ClientsGetLocalListForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    get_locallist(cpnumber)

    return super().form_valid(form) 

class SendLocalListView(FormView):
  template_name = 'clients_sendlocallist.html'
  form_class = ClientsSendLocalListForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    list_version = int(form.data.get('list_version'))
    update_type = form.data.get('update_type')
    local_authorization_list = form.data.get('local_authorization_list')
    send_locallist(cpnumber, list_version, update_type, eval(local_authorization_list))

    return super().form_valid(form) 

class ClientsResetView(FormView):
  template_name = 'clients_reset2.html'
  form_class = ClientsResetForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    reset_type = form.data.get('reset_type')
    reset_cpinfo(cpnumber, reset_type)

    return super().form_valid(form) 

class UpdateFirmwareView(FormView):
  template_name = 'clients_updatefirmware.html'
  form_class = ClientsUpdateFirmwareForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    location = form.data.get('location')
    retrieve_date = form.data.get('retrieve_date')

    update_firmware(cpnumber, location, retrieve_date)

    return super().form_valid(form) 

class GetDiagnosticsView(FormView):
  template_name = 'clients_getdiagnostics.html'
  form_class = ClientsGetDiagForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    location = form.data.get('location')

    get_diagnostics(cpnumber, location)

    return super().form_valid(form) 

class ReserveNowView(FormView):
  template_name = 'clients_reservenow.html'
  form_class = ClientsReserveNowForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    connector_id = int(form.data.get('connector_id'))
    expiry_date = form.data.get('expiry_date')
    id_tag = form.data.get('id_tag')
    parent_id_tag = form.data.get('parent_id_tag')
    reservation_id = int(form.data.get('reservation_id'))

    reserve_now(cpnumber, connector_id, expiry_date, id_tag, parent_id_tag, reservation_id)

    return super().form_valid(form) 

class CancelReservationView(FormView):
  template_name = 'clients_cancelreservation.html'
  form_class = ClientsCancelReservationForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    reservation_id = int(form.data.get('reservation_id'))

    cancel_reservation(cpnumber, reservation_id)

    return super().form_valid(form) 

class TriggerMessageView(FormView):
  template_name = 'clients_triggermessage.html'
  form_class = ClientsTriggerMessageForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    requested_message = form.data.get('requested_message')
    trigger_message(cpnumber, requested_message)

    return super().form_valid(form) 

class ChangeAvailableView(FormView):
  template_name = 'clients_changeavailable.html'
  form_class = ClientsChangeAvailableForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    connector_id = int(form.data.get('connector_id'))
    op_type = form.data.get('op_type')

    change_available(cpnumber, connector_id, op_type)

    return super().form_valid(form) 

# class ClientsFwupdateView(FormView):
#   template_name = 'clients_fwupdate.html'
#   form_class = ClientsResetForm
#   success_url = '/clients'

#   def form_valid(self, form):
#     cpnumber = form.data.get('cpnumber')
#     update_clients(cpnumber)

#     return super().form_valid(form) 


class GetCmpScheduleView(FormView):
  template_name = 'charging_profile.html'
  form_class = CompositeScheduleForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    connectorId = form.data.get('connector_id')
    duration = form.data.get('duration')

    get_composite_schedule(cpnumber, connectorId, duration)

    return super().form_valid(form) 

class DataTransferView(FormView):
  template_name = 'clients_datatransfer.html'
  form_class = DataTransferForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    vendor_id = form.data.get('vendor_id')
    message_id = form.data.get('message_id')
    data = form.data.get('data')

    data_transfer(cpnumber, vendor_id, message_id, data)

    return super().form_valid(form) 

class SetChgProfileView(FormView):
  template_name = 'charging_profile.html'
  form_class = ChargingProfileForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    profile = {
      'connectorId': form.data.get('connector_id'),
      'chargingProfilePurpose': form.data.get('charging_profile_purpose'),      # ChargePointMaxProfile, TxDefaultProfile, TxProfile
      'chargingProfileKind': form.data.get('charging_profile_kind'),            # Absolute, Recurring, Relative 
      'chargingProfileId': 1,
      'stackLevel': 1,
      'chargingSchedule': {
        'duration': int(form.data.get('duration')),
        'chargingRateUnit': 'W',
        'chargingSchedulePeriod': [
          {
            'startPeriod': 1,
            'limit': 8.1,
          },
        ]
      }
    }
    set_charging_profile(cpnumber, profile)

    return super().form_valid(form) 

class ClearChgProfileView(FormView):
  template_name = 'clear_charging_profile.html'
  form_class = ClearChargingProfileForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    connectorId = form.data.get('connector_id')
    id = form.data.get('profile_id')

    clear_charging_profile(cpnumber, connectorId, id)

    return super().form_valid(form) 