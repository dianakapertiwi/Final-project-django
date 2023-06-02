from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def pengguna(request):
    context = {
        'nama' = 'diana'
    }
    
    template = loader.get_template('pengguna.html')
    return HttpResponse(template.render(context, request))

def penggunadb(request):
    data = Pengguna.objects.all().values()[2]
    context = {
        'data_pengguna': data
    }

    template = loader.get_template('pengguna.html')
    return HttpResponse(template.render(context, request))
