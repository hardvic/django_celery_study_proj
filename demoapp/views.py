# !/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

from demoapp.tasks import add

# Create your views here.


def index(request):
    p1 = request.GET.get('p1')
    p2 = request.GET.get('p2')
    add.delay(p1, p2)
    return HttpResponse("hi, you're in djcelery_pro index")
