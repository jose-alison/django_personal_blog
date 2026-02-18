from django.views.generic import (ListView, CreateView, DetailView, DeleteView, UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import User
from .forms import UserCreateForm, UserUpdateForm

class SuperUserMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class UserCreateView(SuperUserMixin, CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('users:list')

user_create_view = UserCreateView.as_view()


class UserListView(SuperUserMixin, ListView):
    model = User
    template_name = 'users/list.html'
    context_object_name = 'users'
    paginate_by = 25

user_list_view = UserListView.as_view()


class UserDetailView(SuperUserMixin, DetailView):
    model = User
    template_name = 'users/detail.html'

user_detail_view = UserDetailView.as_view()


class UserDeleteView(SuperUserMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'

    def get_queryset(self):
        qs = super().get_queryset()
        qs.exclude(pk=self.request.user.pk)

user_delete_view = UserDeleteView.as_view()


class UserUpdateView(SuperUserMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users:list')

user_update_view = UserUpdateView.as_view()
