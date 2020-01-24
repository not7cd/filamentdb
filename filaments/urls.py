from django.urls import path

from . import views

SPOOL_URL_NAME = "spool"

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('spool/<int:spool_id>/', views.spool_detail, name='spool'),
    path('add', views.spool_add, name='spool_add')
]
