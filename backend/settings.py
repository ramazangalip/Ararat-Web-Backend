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

# settings.py dosyanızdaki DATABASES bloğu

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        
        'NAME': 'vc34n3dhidmi4ddm_medium', # Açıkça yazılan DB adı
        'USER': 'ADMIN', # Açıkça yazılan kullanıcı
        'PASSWORD': 'BÜ.Btmyo.2025?', # Açıkça yazılan parola
        
        'OPTIONS': {
           'config_dir': str(BASE_DIR / 'wallet'), # Çözülmüş wallet yolu
           'wallet_location': str(BASE_DIR / 'wallet'), # Çözülmüş wallet yolu
           'wallet_password': 'Btmyo.2025', # Açıkça yazılan wallet parolası
           
           # KRİTİK EKLEME: Bu, Django/oracledb uyumsuzluğunu aşmayı hedefler.
           'threaded': True,
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
