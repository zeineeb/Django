from django.contrib import admin , messages
from .models import *

# Register your models here.
class ParticipationInline(admin.TabularInline): 
    model = Participation
    extra =1
    readonly_fields =("date_participation",)
    can_delete=True
class ParticipantFilter(admin.SimpleListFilter):
    title="Participant"
    parameter_name ="nbe_participant"
    def lookups(self , request, modelAdmin):
        return (('0', ('0 Participant',)),
        ('more',('more Participant',)), )

    def queryset(self , request , querySet):
        if self.value() == '0':
            return querySet.filter(nbe_participant__exact = 0)
        if self.value() == 'more':
            return querySet.filter(nbe_participant__gt = 0)   


class DateFilter(admin.SimpleListFilter):
    title="Event Date"
    parameter_name ="evt_date"
    def lookups(self , request, modelAdmin):
        return(
            ('PostEvent','Post Event',),
            ('TodayEvent','Today Event',),
            ('UpcomingEvent','Upcoming Event',)
        )

    def queryset(self , request , querySet):
        if self.value() == 'PostEvent':
            return querySet.filter(evt_date__lt = date.today())
        if self.value() == 'TodayEvent':
            return querySet.filter(evt_date__exact = date.today()) 
        if self.value() == 'UpcomingEvent':
            return querySet.filter(evt_date__gt = date.today()) 

def UpdateState(modelAdmin , request , querySet):
    row_updated = querySet.update(state=False)
    if row_updated == 1 :
        msg="un seul evenement"
    else :
        msg ="plusieurs"
    return messages.success(request , message ='%s updated'% msg)

UpdateState.short_description='refuse'
def Accept(self , request , querySet):
    row_updated = querySet.update(state=True)
    if row_updated == 1 :
        msg="un seul evenement"
    else :
        msg ="plusieurs"
    return messages.success(request , message ='%s updated'% msg)

@admin.action(description = "Accept")
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):


    def Participant_number(self,obj):
        val=obj.participations.count()
        return val
    list_display=['title','category','state','Participant_number','created_at','evt_date']
    list_filter=['state','category', ParticipantFilter ,DateFilter]
    search_fields=['title','category']
    list_per_page= 5
    ordering=['-title','-created_at','-evt_date']
    readonly_fields=['updated_at','created_at']
    autocomplete_fields=['organise']
    inlines=[ParticipationInline]
    actions=[UpdateState , Accept]
    actions_on_bottom=True
    actions_on_top=False


    fieldsets = [
        ['Event State',{
            'fields':['state',]
        } ],

        ['About' , {
            'classes':['collapse'],
            'fields':('title','description','image','category','nbe_participant'  , 'organise')
        }],

        ['Date' , {
            'fields':['evt_date','updated_at','created_at']
        }]
    ]



class ParticipationEvent(admin.ModelAdmin):
    admin.site.register(Participation)
