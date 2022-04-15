from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views import generic as views

from pythonMyProject.bikes.forms import CreateBikesForm, SellBikeCreateForm
from pythonMyProject.bikes.models import Bike, SellBike
from pythonMyProject.common.helpers import DisableFieldsFormMixin
from pythonMyProject.common.mixins import StaffPermissionsMixin


class CreateBikeView(LoginRequiredMixin, StaffPermissionsMixin, views.CreateView):
    permission_required = ['bikes.add_bike']

    form_class = CreateBikesForm
    template_name = 'bikes/create_bike.html'
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditBikeView(LoginRequiredMixin, StaffPermissionsMixin, views.UpdateView):
    permission_required = ['bikes.change_bike']

    model = Bike
    template_name = 'bikes/edit_bike.html'
    fields = ('name', 'type', 'description', 'image',)

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.user_id})


class DeleteBikeView(LoginRequiredMixin, StaffPermissionsMixin, views.DeleteView):
    permission_required = ['bikes.delete_bike']

    model = Bike
    template_name = 'bikes/delete_bike.html'
    fields = '__all__'

    # success_url = reverse_lazy('profile details')

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.user_id})


class SellBikeView(LoginRequiredMixin, StaffPermissionsMixin, views.CreateView):
    permission_required = ['bikes.add_sellbike']

    form_class = SellBikeCreateForm
    template_name = 'bikes/sell_bike.html'
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditSellBikeView(LoginRequiredMixin, StaffPermissionsMixin, views.UpdateView):
    permission_required = ['bikes.change_sellbike']

    model = SellBike
    template_name = 'bikes/edit_sell_bike.html'
    fields = ('name', 'type', 'frame', 'fork', 'rear_shock', 'brakes', 'drivetrain', 'image', 'price',)
    success_url = reverse_lazy('dashboard')


class DeleteSellBikeView(LoginRequiredMixin, StaffPermissionsMixin, DisableFieldsFormMixin, views.DeleteView):

    permission_required = ['bikes.delete_sellbike']

    model = SellBike
    template_name = 'bikes/delete_sell_bike.html'
    fields = ('name', 'type', 'frame', 'fork', 'rear_shock', 'brakes', 'drivetrain', 'image', 'price',)
    success_url = reverse_lazy('dashboard')

