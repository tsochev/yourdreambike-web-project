
from django.urls import reverse_lazy
from django.views import generic as views

from pythonMyProject.bikes.forms import CreateBikesForm, SellBikeCreateForm, EditBikeForm, DeleteBikeForm
from pythonMyProject.bikes.models import Bike


class SellBikeView(views.CreateView):
    form_class = SellBikeCreateForm
    template_name = 'bikes/sell_bike.html'
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class CreateBikeView(views.CreateView):
    form_class = CreateBikesForm
    template_name = 'bikes/create_bike.html'
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditBikeView(views.UpdateView):
    model = Bike
    template_name = 'bikes/edit_bike.html'
    fields = ('name', 'type', 'description', 'image', )

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.user_id})


class DeleteBikeView(views.DeleteView):
    model = Bike
    template_name = 'bikes/delete_bike.html'
    fields = '__all__'
    # success_url = reverse_lazy('profile details')

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.user_id})
