from django.urls import path

from . import views

SPOOL_URL_NAME = "spool"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="index"),
    path("spool/<int:pk>/", views.SpoolDetailView.as_view(), name="spool-detail"),
    path("add", views.SpoolCreate.as_view(), name="spool-create"),
    path("update/<int:pk>", views.SpoolUpdate.as_view(), name="spool-update"),
    path("delete/<int:pk>", views.SpoolDelete.as_view(), name="spool-delete"),
    path("search", views.search, name="spool-search"),
    path("stash", views.SpoolPrivateListView.as_view(), name="spool-list-private"),
    path("materials", views.MaterialListView.as_view(), name="material-list"),
    path("material", views.MaterialCreate.as_view(), name="material-create"),
    path("material-variant", views.VariantCreate.as_view(), name="variant-create"),
]
