from django.urls import path
from . import views

urlpatterns = [
  path('', views.ClientsList.as_view()),
  path('<int:pk>/', views.ClientsDetail.as_view()),
  path('<int:pk>/delete/', views.ClientsDeleteView.as_view()),
  path('<int:pk>/remo_scs_cpf/', views.RemoStartChargeView.as_view()),
  path('<int:pk>/remo_stop_cs/', views.RemoStopChargeView.as_view()),
  path('<int:pk>/unlock_connector/', views.UnlockConnView.as_view()),
  path('<int:pk>/clearcache/', views.ClientsClearcacheView.as_view()),
  path('<int:pk>/getconf/', views.GetConfView.as_view()),
  path('<int:pk>/setconf/', views.SetConfView.as_view()),
  path('<int:pk>/setchargingprofile/', views.SetChgProfileView.as_view()),
  path('<int:pk>/clearchargingprofile/', views.ClearChgProfileView.as_view()),
  path('<int:pk>/getlocallistversion/', views.GetLocalListVersionView.as_view()),
  path('<int:pk>/sendlocallist/', views.SendLocalListView.as_view()),
  path('<int:pk>/updatefirmware/', views.UpdateFirmwareView.as_view()),
  path('<int:pk>/getdiagnostics/', views.GetDiagnosticsView.as_view()),
  path('<int:pk>/reservenow/', views.ReserveNowView.as_view()),
  path('<int:pk>/cancelreservation/', views.CancelReservationView.as_view()),
  path('<int:pk>/triggermessage/', views.TriggerMessageView.as_view()),
  path('<int:pk>/changeavailable/', views.ChangeAvailableView.as_view()),
  path('<int:pk>/getcompositeschedule/', views.GetCmpScheduleView.as_view()),
  path('<int:pk>/datatransfer/', views.DataTransferView.as_view()),
  path('<int:pk>/reset/', views.ClientsResetView.as_view()),
  # path('simul/', views.index),
  # path('simul/<str:cpnumber>/', views.index),
]