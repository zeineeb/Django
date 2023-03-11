from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Event, Participation
from  django.views.generic import ListView,DetailView, CreateView, UpdateView , DeleteView
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date
# Create your views here.
#Views funtion based
def HomePage(request):
    return HttpResponse('<h1>Hello from home page</h1>')

def ListEvent(request):
    list =Event.objects.filter(state=True)
    return render(request,'events/EventList.html' , {'events' : list})


def add_event(req):
    form =EventForm()
    if req.method =="POST" :
        form =EventForm(req.POST,req.FILES)
        if form.is_valid():
            # print(**form.cleaned_data)
            Event.objects.create(**form.cleaned_data)
            return redirect('list_events_view')
        else:
            print(form.errors)
    return render(req, "events/event_form.html",{'form':form})      

#Views Class Based

class ListEventView(LoginRequiredMixin ,ListView):
    login_url="login"
    model =Event
    template_name ="events/EventList.html"
    context_object_name ="events"
    # def get_queryset(self):
    #     return Event.objects.filter(state=True)

class DetailEventView(LoginRequiredMixin,DetailView):
    login_url="login"
    model=Event
    template_name ="events/DetailsEvent.html"
    context_object_name ="event"

@login_required(login_url="/users/login")
def create_event(req):
    if req.method == "GET": 
        form= EventModelForm()
        return render(req, "events/event_form.html",{'form':form})
    if req.method == "POST":
        form = EventModelForm(req.POST, req.FILES)
        if form.is_valid():
            Event = form.save(commit=False)
            Event.save()
            return redirect('list_event_view')
        else: 
            return render(req, "events/event_form.html",{'form':form})   

class CreateEvent(LoginRequiredMixin,CreateView):
    login_url="login"
    model=Event
    template_name= "events/event_form.html"
    form_class= EventModelForm
    success_url= reverse_lazy('list_events_view')


class UpdateEvent(LoginRequiredMixin,UpdateView):
    login_url="login"
    model=Event
    template_name= "events/event_form.html"
    form_class= EventModelForm
    success_url= reverse_lazy('list_events_view')

class DeleteEvent(LoginRequiredMixin,DeleteView):
    model=Event
    success_url= reverse_lazy('list_events_view')

def participate(req ,eventId):
    event=Event.objects.get(id=eventId)
    user=req.user
    if Participation.objects.filter(Person=user , event=event).count()==0:
        event.nbe_participant+=1
        event.save()
        part=Participation.objects.create(Person=user, event=event , date_participation=date.today)
        return redirect("list_events_view")
    else:
        return redirect("list_events_view")




    