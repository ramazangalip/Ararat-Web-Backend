from django.contrib import admin
from .models import *

@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    list_display = ('slogan_tr',)

@admin.register(FeatureCard)
class FeatureCardAdmin(admin.ModelAdmin):
   
    list_display = ('title_tr', 'order', 'icon_name') 
    
  
    list_editable = ('order', 'icon_name')
@admin.register(ContactPageContent)
class ContactPageContentAdmin(admin.ModelAdmin):
    list_display = ('page_title_tr', 'whatsapp_number')

@admin.register(WhyAraratNameContent)
class WhyAraratNameContentAdmin(admin.ModelAdmin):
    list_display = ('title_tr', 'title_en')

@admin.register(WhatIsAraratTokenContent)
class WhatIsAraratTokenContentAdmin(admin.ModelAdmin):
    list_display = ('title_tr', 'title_en')



@admin.register(PurposePageContent)
class PurposePageContentAdmin(admin.ModelAdmin):
   
    list_display = ('main_text_tr',) 


@admin.register(TimelineCard)
class TimelineCardAdmin(admin.ModelAdmin):

    list_display = ('title_tr', 'order') 
    list_editable = ('order',)