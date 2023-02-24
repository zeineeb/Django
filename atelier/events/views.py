from django.shortcuts import render
from django.http import HttpResponse


def HomePage(req):
    return HttpResponse("<h1> hi , Home Page </h1>")

def testId (req , id):
    res = 'resultat avec id %s'
    return HttpResponse(res % id)

def RenderList(req):
    list = [
    {
    'title': 'Event 1',
    'description': 'description 1',
    },
    {
    'title': 'Event 2',
    'description': 'description 2',
    },
    {
    'title': 'Event 3',
    'description': 'description 3',
    }
    ]
    return render(req , 'events/list.html',{'events':list})

# Create your views here.

