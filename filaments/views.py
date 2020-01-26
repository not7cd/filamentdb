from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from .models import Spool, Material
from .forms import SpoolForm, MaterialForm, VariantForm


# ...
def detail(request, spool_id):
    return HttpResponse("You're looking at question %s." % spool_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def index(request):
    latest_spool_list = Spool.objects.order_by("-pub_date")[:5]
    context = {"latest_spool_list": latest_spool_list}
    return render(request, "index.html", context)


class MaterialListView(ListView):
    model = Material

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@login_required()
class MaterialCreate(CreateView):
    form_class = MaterialForm
    template_name = "filaments/material_form.html"


@login_required()
class VariantCreate(CreateView):
    form_class = VariantForm
    template_name = "filaments/variant_form.html"


def spool_detail(request, spool_id):
    spool = Spool.objects.get(pk=spool_id)
    context = {"spool": spool}
    return render(request, "spool_detail.html", context)


@login_required
class SpoolCreate(CreateView):
    form_class = SpoolForm
    template_name = "filaments/spool_form.html"
