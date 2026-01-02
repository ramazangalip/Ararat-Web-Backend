from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# =====================
# SECURITY
# =====================

SECRET_KEY = 'django-insecure-5y$_q8(fi8_o^8gjy3&h&b&b8&f6u)^_=k#61a6m-71smn6iv-'

DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "*.render.com",
    "api.ararattoken.com", 
    
]

CSRF_TRUSTED_ORIGINS = [
    "https://ararattoken.com",
    
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
    'whitenoise.middleware.WhiteNoiseMiddleware',
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
    "https://ararattoken.com",          
    "https://www.ararattoken.com",
    "https://ararat-web-1.onrender.com/"
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


# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres.fqoeoyfyvugqthmcbzlh', # Kullanıcı adınızı bu şekilde kullanın
        'PASSWORD': 'R.s.17080607',
        'HOST': 'aws-1-ap-south-1.pooler.supabase.com', 
        'PORT': '6543', # KRİTİK DÜZELTME
    }
}


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles" # Bu satır aslında mevcuttu, emin olmak için ekledim.

# WhiteNoise için gerekli ayar
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# =====================
# INTERNATIONALIZATION
# =====================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
