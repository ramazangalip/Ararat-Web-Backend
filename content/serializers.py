# content/serializers.py

from rest_framework import serializers
from .models import *

# 1. Ana Sayfa İçeriği Serializer'ı
class HomePageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePageContent
        # Tüm alanlari API'ye aciyoruz
        fields = '__all__' 
        # API'den veri cekilecegi icin ('GET'), okuma izni veriyoruz
        read_only_fields = ['slogan_tr', 'slogan_en', 'subheadline_tr', 'subheadline_en'] 

# 2. Ozellik Kartlari Serializer'i
class FeatureCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureCard
        fields = '__all__'
        read_only_fields = ['order', 'icon_name', 'title_tr', 'title_en', 'description_tr', 'description_en']

# 3. Iletisim Sayfasi Icerigi Serializer'i
class ContactPageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPageContent
        fields = '__all__'
        read_only_fields = ['page_title_tr', 'page_title_en', 'warning_text_tr', 'warning_text_en', 'whatsapp_number']


# content/serializers.py



class WhyAraratNameContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyAraratNameContent
        fields = '__all__'

class WhatIsAraratTokenContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatIsAraratTokenContent
        fields = '__all__'


class PurposePageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurposePageContent
        fields = '__all__'

class TimelineCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimelineCard
        fields = '__all__'