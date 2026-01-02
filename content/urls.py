# content/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    
    path('home/', HomePageContentDetail.as_view(), name='home-content-detail'), 
    

    path('features/', FeatureCardList.as_view(), name='feature-card-list'), 
    
  
    path('contact/', ContactPageContentDetail.as_view(), name='contact-content-detail'),
    path('why-ararat/', WhyAraratNameContentDetail.as_view(), name='why-ararat-content'),
    path('what-is-token/', WhatIsAraratTokenContentDetail.as_view(), name='what-is-token-content'),

   
    path('purpose/', PurposePageContentDetail.as_view(), name='purpose-content'),
    path('purpose/timeline/', TimelineCardList.as_view(), name='timeline-card-list'),

]