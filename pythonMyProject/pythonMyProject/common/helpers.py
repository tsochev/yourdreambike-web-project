from django import forms
from django.shortcuts import render


class BootstrapFormMixin:
    fields = {}

    def _init_bootstrap_form_control(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            if 'class ' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += 'form-control'


class DisableFieldsFormMixin:
    disabled_fields = '__all__'
    fields = {}

    def _init_disabled_fields(self):
        for name, field in self.fields.items():
            if self.disabled_fields != '__all__' and name not in self.disabled_fields:
                continue

            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attr', {})
            if isinstance(field, forms.ChoiceField):
                field.widget.attrs['disabled'] = 'disabled'
            else:
                field.widget.attrs['readonly'] = 'readonly'


def error_404(request, exception):
    return render(request, '403_no_permission.html')