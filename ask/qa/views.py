from django.shortcuts import render
from django.http import HttpResponse
def test(request, *args, **kwargs):
    return HttpResponse('OK')

def error(request,*args, **kwargs):
    return HttpResponse('Not ok')
# Create your views here.
