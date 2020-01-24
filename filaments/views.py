from django.http import HttpResponse
from django.shortcuts import render
from .models import Spool

# ...
def detail(request, spool_id):
    return HttpResponse("You're looking at question %s." % spool_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def index(request):
    latest_spool_list = Spool.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_spool_list}
    return render(request, 'index.html', context)


def spool_detail(request, spool_id):
    spool = Spool.objects.get(pk=spool_id)
    context = {"spool": spool}
    return render(request, 'spool_detail.html', context)

def spool_add(request):
    return render(request, 'spool_add.html')
