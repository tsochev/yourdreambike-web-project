from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

from pythonMyProject.accounts.models import Profile
from pythonMyProject.common.helpers import BootstrapFormMixin

UserModel = get_user_model()


class CreateProfileForm(BootstrapFormMixin, UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LEN,
    )

    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LEN,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_control()

    def save(self, commit=True):
        user = super().save(commit=commit)

        group = Group.objects.get(name='regular_user')
        user.groups.add(group)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            user=user,
        )
        if commit:
            profile.save()

        return user

    class Meta:
        model = UserModel
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name',)


class EditProfileForm(forms.ModelForm):
    model = Profile
    fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        # pets = list(self.instance.pet_set.all())
        # should be done with signals
        # because this breaks the abstraction of the auth app
        # PetPhoto.objects.filter(tagged_pets__in=pets) \
        #     .delete()

        self.instance.delete()  # instance is a Profile

        return self.instance

    class Meta:
        model = Profile
        fields = ()
