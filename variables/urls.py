from django.urls import path
from . import views

urlpatterns = [
  path('', views.VariablesList.as_view()),
  path('register/', views.VariablesCreateView.as_view()),
  path('<str:pk>/', views.VariablesDetail.as_view()),
  path('<int:pk>/update', views.VariablesUpdateView.as_view()),
  path('<int:pk>/delete/', views.VariablesDeleteView.as_view()),
  # path('simul/', views.index),
  # path('simul/<str:cpnumber>/', views.index),
]