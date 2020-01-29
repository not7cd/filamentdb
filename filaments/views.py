from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, OuterRef, Sum, Subquery
from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, FormMixin, UpdateView

from .forms import SpoolForm, MaterialForm, VariantForm
from .models import Spool, Material


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        spools = Spool.objects.filter(variant__material=OuterRef('pk')).order_by().values('variant__material')
        # spools_with_mass = Spool.filter.(total_mass=Sum('mass_net')).values('total_mass')
        # print(total_spools)
        plastic_stats = Material.objects.values("plastic").annotate(total_mass=Sum("variant__spool__mass_net"))
        print(plastic_stats)
        context['plastic_stats'] = plastic_stats
        context['latest_spool_list'] = Spool.objects.order_by("-pub_date")[:5]\
            .select_related('variant')\
            .select_related('variant__material')
        return context


def search(request):
    try:
        q = request.GET['q']
        spools = Spool.objects.filter(
            Q(variant__material__brand__icontains=q) | Q(variant__name__icontains=q) | Q(comment__icontains=q)
        ).select_related('variant').select_related('variant__material')
        return render(request, 'search_results.html', {'object_list': spools, 'q': q})
    except KeyError:
        return render(request, 'search_results.html', {})


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


class SpoolUpdate(LoginRequiredMixin, UpdateView):
    model = Spool
    form_class = SpoolForm
    template_name = "filaments/spool_update.html"


class SpoolPrivateListView(LoginRequiredMixin, ListView):
    model = Spool
    template_name_suffix = "_private_list"

    def get_queryset(self):
        return Spool.objects.filter(
            owner__user_id=self.request.user.ownerprofile.id
        )

