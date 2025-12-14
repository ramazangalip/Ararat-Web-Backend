"""
URL configuration for backend project.
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings # 💡 Yeni: settings'i içeri aktar
from django.conf.urls.static import static # 💡 Yeni: static() fonksiyonunu içeri aktar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/content/', include('content.urls')),
]

# 💡 YENİ EKLENEN KISIM: Medya dosyalarini gelistirme ortaminda sunmak icin
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    # Not: Statik dosyalar için de benzer bir satır eklenebilir, 
    # ancak genellikle 'runserver' statik dosyalari otomatik sunar.
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)