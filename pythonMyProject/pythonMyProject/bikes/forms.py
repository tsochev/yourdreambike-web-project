from django import forms

from pythonMyProject.bikes.models import Bike, SellBike
from pythonMyProject.common.helpers import BootstrapFormMixin, DisableFieldsFormMixin


class CreateBikesForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_control()

    def save(self, commit=True):
        bike = super().save(commit=False)

        bike.user = self.user
        if commit:
            bike.save()

        return bike

    class Meta:
        model = Bike
        exclude = ('user', )


class EditBikeForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Bike
        exclude = ('user', )


class DeleteBikeForm(BootstrapFormMixin, DisableFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_control()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Bike
        exclude = ('user', )


class SellBikeCreateForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_control()

    def save(self, commit=True):
        sell_bike = super().save(commit=False)

        sell_bike.user = self.user
        if commit:
            sell_bike.save()

        return sell_bike

    class Meta:
        model = SellBike
        exclude = ('user', )

