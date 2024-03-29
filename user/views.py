from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from .models import User

class UserList(ListView):
  model = User
  template_name='user.html'
  context_object_name = 'userList'
  paginate_by = 2
  queryset = User.objects.all()

  def get_queryset(self):
    queryset = User.objects.all()
    query = self.request.GET.get("q", None)
    if query is not None:
      queryset = queryset.filter(
        Q(userid__icontains=query)
        # Q(name__icontains=query) |
        # Q(phone__icontains=query)
      )
    return queryset
  
class UserCreateView(CreateView):
  model = User
  template_name = 'user_register.html'
  fields = ['userid', 'password', 'name', 'email', 'phone',]
  success_url = '/user'

class UserDeleteView(DeleteView):
    model = User
    template_name='user_confirm_delete.html'
    success_url = '/user'