from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, FormMixin, ModelFormMixin
from django.shortcuts import render
from .models import Spool, Material
from .forms import SpoolForm, MaterialForm, VariantForm


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_spool_list'] = Spool.objects.order_by("-pub_date")[:5]
        return context


class MaterialListView(ListView):
    model = Material

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MaterialCreate(LoginRequiredMixin, CreateView):
    form_class = MaterialForm
    success_url = "/materials"
    template_name = "filaments/material_form.html"


class VariantCreate(LoginRequiredMixin, CreateView):
    form_class = VariantForm
    template_name = "filaments/variant_form.html"


class SpoolDetailView(DetailView):
    model = Spool


class SpoolCreate(LoginRequiredMixin, CreateView):
    form_class = SpoolForm
    template_name = "filaments/spool_form.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner_id = self.request.user.ownerprofile.id
        self.object.save()
        return FormMixin.form_valid(self, form)
