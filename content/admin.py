from django.contrib import admin
from .models import *

@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    list_display = ('slogan_tr',)

@admin.register(FeatureCard)
class FeatureCardAdmin(admin.ModelAdmin):
    # 'order' artik ilk sirada degil.
    list_display = ('title_tr', 'order', 'icon_name') 
    
    # 'order' hala duzenlenebilir.
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
    # 💡 DÜZELTME: Başlıklar kaldırıldığı için, list_display'de sadece metin gösteriliyor.
    list_display = ('main_text_tr',) 
    # Veya sadece '__str__' metodunu kullanır. list_display'i boş bırakırsanız da çalışır.
    # fields = ('main_text_tr', 'main_text_en', 'main_image')

@admin.register(TimelineCard)
class TimelineCardAdmin(admin.ModelAdmin):
    # 💡 DÜZELTME: list_display ve list_editable sadece 'order' alanını kullanıyor.
    list_display = ('title_tr', 'order') 
    list_editable = ('order',)