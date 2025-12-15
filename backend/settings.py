from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# =====================
# SECURITY
# =====================

SECRET_KEY = os.environ.get("SECRET_KEY", "unsafe-dev-key")

DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".fly.dev",
    "api.ararattoken.com", 
]

CSRF_TRUSTED_ORIGINS = [
    "https://ararattoken.com",
    "https://*.fly.dev",
]

# =====================
# APPLICATIONS
# =====================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'rest_framework',

    'content',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# =====================
# CORS
# =====================

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "https://ararattoken.com",          # 🔴 frontend domain
    "https://www.ararattoken.com",
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

# =====================
# URL / WSGI
# =====================

ROOT_URLCONF = 'backend.urls'
WSGI_APPLICATION = 'backend.wsgi.application'

# =====================
# TEMPLATES
# =====================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# =====================
# DATABASE (Oracle Autonomous)
# =====================
# settings.py dosyanızda

# =====================
# DATABASE (Oracle Autonomous) - GÜVENLİ VE FLY.IO UYUMLU AYAR
# =====================

# Fly.io Buildpack, proje dosyalarını /workspace veya /app/code dizinlerine kopyalar.
# En güvenilir yol: /code/wallet (Çoğu Fly.io ve Buildpack ortamı için çalışır)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        
        # HASSAS VERİLER SADECE ORTAM DEĞİŞKENLERİNDEN OKUNMALI
        'NAME': os.environ.get("ORACLE_DB_NAME"), # vc34n3dhidmi4ddm_medium olmalı
        'USER': os.environ.get("ORACLE_DB_USER"), # ADMIN olmalı
        'PASSWORD': os.environ.get("ORACLE_DB_PASSWORD"), # Parolanız olmalı
        
        'OPTIONS': {
            # Önceki Windows yolu sızıntısını engellemek için, kesin Linux yolu (Hardcode)
            'config_dir': '/code/wallet',
            'wallet_location': '/code/wallet',
            
            # PAROLA yine Ortam Değişkeninden okunmalı
            'wallet_password': os.environ.get("ORACLE_WALLET_PASSWORD"), 
        }
    }
}

# =====================
# STATIC / MEDIA
# =====================

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# =====================
# INTERNATIONALIZATION
# =====================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
