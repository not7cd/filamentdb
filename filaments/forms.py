from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.forms import ModelForm

from .models import Material, Variant, Spool


class MaterialForm(ModelForm):
    class Meta:
        model = Material
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(MaterialForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save"))


class VariantForm(ModelForm):
    class Meta:
        model = Variant
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(VariantForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save"))


class SpoolForm(ModelForm):
    class Meta:
        model = Spool
        exclude = ["owner", "pub_date"]

    def __init__(self, *args, **kwargs):
        super(SpoolForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save"))
