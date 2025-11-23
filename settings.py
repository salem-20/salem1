# settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third party apps
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    # Your App
    'restaurant', 
]

# DRF Configuration for Authentication
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

# DJOSER Configuration
DJOSER = {
    "USER_ID_FIELD": "username"
}

# Database Configuration (MySQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'littlelemon_db', # Make sure you create this DB in MySQL Workbench
        'USER': 'root',           # Your MySQL username
        'PASSWORD': 'password',   # Your MySQL password
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

STATIC_URL = 'static/'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], # Important for static HTML requirement
        'APP_DIRS': True,
        # ... (rest of template config)
    },
]