from django.contrib import admin
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
    title = 'Event Date'
    parameter_name = 'Evt_date' 
    def lookups(self, request, model_admin):
        return (
            ('PostEvent', 'Post Event',),
            ('TodayEvent', 'Today Event'),
            ('UpcomingEvent', 'Upcoming Event')
        )
    def queryset(self, request, queryset):
        if self.value() == 'PostEvent':
            return queryset.filter(evt_date__lt=date.today())
        if self.value() == 'TodayEvent':
            return queryset.filter(evt_date__exact=date.today())
        if self.value() == 'UpcomingEvent':
            return queryset.filter(evt_date__gt=date.today())

    def queryset(self , request , querySet):
        if self.value() == '0':
            return querySet.filter(nbe_participant__exact = 0)
        if self.value() == 'more':
            return querySet.filter(nbe_participant__gt = 0)  


def UpdateState(Modeladmin,request,querySet):
    rows_update = querySet.update(state=False)
    if rows_update ==1 :
        msg='un seul evement'
    else : 
        msg='plusieurs events'
    return messages.success(request,message='%s modifié' % msg) 

UpdateState.short_description='refuse'

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    def Participant_number(self,obj):
        val=obj.participations.count()
        return val
    list_display =('title','category','state','Participant_number','created_at','evt_date',)
    list_filter =('state','category',)
    search_fields=['title','category']
    list_per_page= 5
    ordering=('-title','-created_at','evt_date',)
    readonly_fields=('updated_at','created_at')
    autocomplete_fields=['organizer']
    fieldsets =(
        
        ('Event State' , {
             'fields' : ('state',)
            
            }) ,
        
        ('About' ,
         {   'classes' :('collapse',),
             'fields' :('title','description','image','category','nbe_participant','organizer')
         }
          ),
        ('Dates',
         { 'classes' :('collapse',),
             'fields' :('evt_date','updated_at','created_at')
         }
         )
        
        
        
        
    )
   
class ParticipationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Participation,ParticipationAdmin)


