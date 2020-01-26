from django.urls import path

from . import views

SPOOL_URL_NAME = "spool"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="index"),
    path("spool/<int:pk>/", views.SpoolDetailView.as_view(), name="spool-detail"),
    path("add", views.SpoolCreate.as_view(), name="spool-create"),
    path("materials", views.MaterialListView.as_view(), name="material-list"),
    path("material", views.MaterialCreate.as_view(), name="material-create"),
    path("material-variant", views.VariantCreate.as_view(), name="variant-create"),
]
