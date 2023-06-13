from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views, get_user_model, login
from django.urls import reverse_lazy
from django.views import generic

from spearfishing_app.accounts.forms import UserCreateForm

UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('index')


class SingInView(generic.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')

    # when new user is created,auto-login
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        login(request, self.object)
        return response


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class UserDetailsView(generic.DetailView):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'


class UserEditView(generic.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'email', 'gender',)

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(generic.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('show index')


def to_github(request):
    return HttpResponseRedirect(
        "https://github.com/GeorgiLukanov87/PythonWeb-Django-Framework/tree/main/petstagram"
    )
