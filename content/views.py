# content/views.py

from rest_framework import generics
from .models import *
from .serializers import *

# Tum listeyi donduren ve yeni eleman eklemeyi saglayan view (sadece FeatureCard icin)
class FeatureCardList(generics.ListCreateAPIView):
    queryset = FeatureCard.objects.all()
    serializer_class = FeatureCardSerializer

# Tek bir objeyi donduren view (Hero ve Contact icin)
class HomePageContentDetail(generics.RetrieveAPIView):
    # API'de sadece ilk (ve tek) objeyi dondurecegiz.
    queryset = HomePageContent.objects.all() 
    serializer_class = HomePageContentSerializer
    
    # Detay View'inde ID kullanmak yerine, objeyi dogrudan cekmek icin
    def get_object(self):
        # Veritabanindaki tek objeyi cek
        return HomePageContent.objects.first() 

class ContactPageContentDetail(generics.RetrieveAPIView):
    queryset = ContactPageContent.objects.all()
    serializer_class = ContactPageContentSerializer

    def get_object(self):
        # Veritabanindaki tek objeyi cek
        return ContactPageContent.objects.first()


class WhyAraratNameContentDetail(generics.RetrieveAPIView):
    queryset = WhyAraratNameContent.objects.all()
    serializer_class = WhyAraratNameContentSerializer
    
    def get_object(self):
        # Veritabanindaki tek objeyi cek
        return WhyAraratNameContent.objects.first()

class WhatIsAraratTokenContentDetail(generics.RetrieveAPIView):
    queryset = WhatIsAraratTokenContent.objects.all()
    serializer_class = WhatIsAraratTokenContentSerializer
    
    def get_object(self):
        # Veritabanindaki tek objeyi cek
        return WhatIsAraratTokenContent.objects.first()
    

# Purpose sayfasinin ana icerigi (Tekil)
class PurposePageContentDetail(generics.RetrieveAPIView):
    queryset = PurposePageContent.objects.all()
    serializer_class = PurposePageContentSerializer
    
    def get_object(self):
        return PurposePageContent.objects.first()

# Zaman Cizelgesi Kartlarinin listesi
class TimelineCardList(generics.ListAPIView):
    queryset = TimelineCard.objects.all()
    serializer_class = TimelineCardSerializer