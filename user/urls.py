from django.urls import path
from . import views

urlpatterns = [
  path('', views.UserList.as_view()),
  path('register/', views.UserCreateView.as_view()),
#   path('<int:pk>/', views.EvchargerDetail.as_view()),
#   path('<int:pk>/update', views.EvcharUpdateView.as_view()),
  path('<int:pk>/delete/', views.UserDeleteView.as_view()),
  # path('<int:pk>/clearcache/', views.ClientsClearcacheView.as_view()),
  # path('<int:pk>/remo_scs_cpf/', views.RemoStartChargeView.as_view()),
  # path('<int:pk>/remo_stop_cs/', views.RemoStopChargeView.as_view()),
  # path('<int:pk>/unlock_connector/', views.UnlockConnView.as_view()),
  # path('<int:pk>/getconf/', views.GetConfView.as_view()),
  # path('<int:pk>/setconf/', views.SetConfView.as_view()),
  # path('<int:pk>/reset/', views.ClientsResetView.as_view()),
  # path('<int:pk>/getcompositeschedule/', views.GetCmpScheduleView.as_view()),
  # path('<int:pk>/setchargingprofile/', views.SetChgProfileView.as_view()),
  # path('<int:pk>/clearchargingprofile/', views.ClearChgProfileView.as_view()),
  # path('simul/', views.index),
  # path('simul/<str:cpnumber>/', views.index),
]