from django.db import models


class HomePageContent(models.Model):

    slogan_tr = models.CharField(max_length=255, verbose_name="Slogan (TR)")
    slogan_en = models.CharField(max_length=255, verbose_name="Slogan (EN)")
    subheadline_tr = models.TextField(verbose_name="Alt Baslik (TR)")
    subheadline_en = models.TextField(verbose_name="Alt Baslik (EN)")

    class Meta:
        verbose_name = "Ana Sayfa Icerigi"
        verbose_name_plural = "Ana Sayfa Icerigi"
    
    def __str__(self):
        return "Ana Sayfa Kahraman Bolumu"


class FeatureCard(models.Model):
    order = models.IntegerField(unique=True, verbose_name="Sirasi")
    icon_name = models.CharField(max_length=50, help_text="Lucide ikon adi (Orn: shield, search)")
    title_tr = models.CharField(max_length=100, verbose_name="Baslik (TR)")
    title_en = models.CharField(max_length=100, verbose_name="Baslik (EN)")
    description_tr = models.TextField(verbose_name="Aciklama (TR)")
    description_en = models.TextField(verbose_name="Aciklama (EN)")

    class Meta:
        ordering = ['order']
        verbose_name = "Ozellik Karti"
        verbose_name_plural = "Ozellik Kartlari"
    
    def __str__(self):
        return f"{self.order}. {self.title_tr}"


class ContactPageContent(models.Model):
    page_title_tr = models.CharField(max_length=100, verbose_name="Sayfa Basligi (TR)")
    page_title_en = models.CharField(max_length=100, verbose_name="Sayfa Basligi (EN)")
    warning_text_tr = models.TextField(verbose_name="Yasal Uyari Metni (TR)")
    warning_text_en = models.TextField(verbose_name="Yasal Uyari Metni (EN)")
    whatsapp_number = models.CharField(max_length=20, help_text="WhatsApp telefon numarasi")

    class Meta:
        verbose_name = "Iletisim Sayfasi Icerigi"
        verbose_name_plural = "Iletisim Sayfasi Icerigi"

    def __str__(self):
        return "Iletisim Sayfasi Verileri"



class WhyAraratNameContent(models.Model):
   
    title_tr = models.CharField(max_length=150, verbose_name="Başlık (TR)")
    title_en = models.CharField(max_length=150, verbose_name="Başlık (EN)")
    text_tr = models.TextField(verbose_name="Paragraf Metni (TR)")
    text_en = models.TextField(verbose_name="Paragraf Metni (EN)")

   
    main_image = models.ImageField(upload_to='content_images/why_ararat/', verbose_name="Sayfa Resmi")

    class Meta:
        verbose_name = "Neden Ararat İsmi Icerigi"
        verbose_name_plural = "Neden Ararat İsmi Icerigi"
    
    def __str__(self):
        return "Neden Ararat İsmi Sayfası Verileri"


class WhatIsAraratTokenContent(models.Model):
  
    title_tr = models.CharField(max_length=150, verbose_name="Başlık (TR)")
    title_en = models.CharField(max_length=150, verbose_name="Başlık (EN)")
    text_tr = models.TextField(verbose_name="Paragraf Metni (TR)")
    text_en = models.TextField(verbose_name="Paragraf Metni (EN)")

    
    main_image = models.ImageField(upload_to='content_images/what_is_token/', verbose_name="Sayfa Resmi")
    

    class Meta:
        verbose_name = "Ararat Token Nedir Icerigi"
        verbose_name_plural = "Ararat Token Nedir Icerigi"
    
    def __str__(self):
        return "Ararat Token Nedir Sayfası Verileri"


class PurposePageContent(models.Model):
    

    main_text_tr = models.TextField(verbose_name="Ana Açıklama Paragrafı (TR)")
    main_text_en = models.TextField(verbose_name="Ana Açıklama Paragrafı (EN)")

    
    main_image = models.ImageField(upload_to='content_images/purpose/', verbose_name="Sayfa Ana Resmi")

    class Meta:
        verbose_name = "Amacimiz Sayfa Icerigi"
        verbose_name_plural = "Amacimiz Sayfa Icerigi"

    def __str__(self):
      
        return "Amacımız Sayfası Verileri"



class TimelineCard(models.Model):
    order = models.IntegerField(verbose_name="Sıra Numarası", unique=True)
    

    title_tr = models.CharField(max_length=100, verbose_name="Kart Başlığı (TR)")
    title_en = models.CharField(max_length=100, verbose_name="Kart Başlığı (EN)")
    

    description_tr = models.TextField(verbose_name="Açıklama Metni (TR)")
    description_en = models.TextField(verbose_name="Açıklama Metni (EN)")
    


    class Meta:
        verbose_name = "Zaman Çizelgesi Kartı"
        verbose_name_plural = "Zaman Çizelgesi Kartları"
        ordering = ['order']

    def __str__(self):
        return f"{self.order}. {self.title_tr}"