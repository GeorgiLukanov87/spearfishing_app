from django.http import HttpResponse
from django.shortcuts import render


# common/views.py


def index(request):
    return HttpResponse('INDEX')
