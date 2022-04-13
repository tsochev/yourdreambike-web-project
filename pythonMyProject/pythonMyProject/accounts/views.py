
from django.contrib.auth import get_user_model, logout, login

from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from pythonMyProject.accounts.forms import CreateProfileForm, DeleteProfileForm
from pythonMyProject.accounts.models import Profile, AppUser
from pythonMyProject.bikes.models import Bike, Order

UserModel = get_user_model()


class UserRegistrationView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'account/registration.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    template_name = 'account/login.html'

    def get_success_url(self):
        return reverse_lazy('dashboard')


def logout_view(request):
    logout(request)
    # messages.success(request, 'You are logout')
    return redirect('home')


class DetailsProfileView(LoginRequiredMixin, views.DetailView):
    model = Profile
    template_name = 'account/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['is_owner'] = self.object.user == self.request.user

        bikes = list(Bike.objects.filter(user_id=self.object.user_id))

        customer = self.request.user.id
        cust_order = Order.objects.filter(customer_id=customer)

        if len(cust_order) > 0:
            # if self.request.user.is_authenticated:

            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            cart_items = order.get_cart_items
        else:

            cart_items = 0

        context.update({
            'is_owner': self.object.user_id == self.request.user.id,
            'bikes': bikes,
            'cart_items': cart_items,
        })

        return context


class EditProfileView(LoginRequiredMixin, views.UpdateView):
    model = Profile
    template_name = 'account/profile_edit.html'
    fields = ('first_name', 'last_name', 'date_of_birth', 'description', 'image',)
    # success_url = reverse_lazy('profile details')

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.pk})

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['first_name'] = 'first_name'


class DeleteProfileView(LoginRequiredMixin, views.DeleteView):
    # the model should be change to UserModel
    model = AppUser
    template_name = 'account/profile_delete.html'
    success_url = reverse_lazy('home')


class ChangePasswordProfileView(LoginRequiredMixin, auth_views.PasswordChangeView):
    template_name = 'account/profile_change_password.html'
