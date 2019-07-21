from django.shortcuts import render
from .models import IA
from django.http import HttpResponse
from django.core import serializers


def ias(request):
    return HttpResponse(serializers.serialize("json", IA.objects.all()))
