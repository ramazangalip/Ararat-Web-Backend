# content/views.py

from rest_framework import generics
from .models import *
from .serializers import *


class FeatureCardList(generics.ListCreateAPIView):
    queryset = FeatureCard.objects.all()
    serializer_class = FeatureCardSerializer


class HomePageContentDetail(generics.RetrieveAPIView):
   
    queryset = HomePageContent.objects.all() 
    serializer_class = HomePageContentSerializer
    
   
    def get_object(self):
       
        return HomePageContent.objects.first() 

class ContactPageContentDetail(generics.RetrieveAPIView):
    queryset = ContactPageContent.objects.all()
    serializer_class = ContactPageContentSerializer

    def get_object(self):
        
        return ContactPageContent.objects.first()


class WhyAraratNameContentDetail(generics.RetrieveAPIView):
    queryset = WhyAraratNameContent.objects.all()
    serializer_class = WhyAraratNameContentSerializer
    
    def get_object(self):
        
        return WhyAraratNameContent.objects.first()

class WhatIsAraratTokenContentDetail(generics.RetrieveAPIView):
    queryset = WhatIsAraratTokenContent.objects.all()
    serializer_class = WhatIsAraratTokenContentSerializer
    
    def get_object(self):
  
        return WhatIsAraratTokenContent.objects.first()
    


class PurposePageContentDetail(generics.RetrieveAPIView):
    queryset = PurposePageContent.objects.all()
    serializer_class = PurposePageContentSerializer
    
    def get_object(self):
        return PurposePageContent.objects.first()


class TimelineCardList(generics.ListAPIView):
    queryset = TimelineCard.objects.all()
    serializer_class = TimelineCardSerializer