# EMAIL_HOST = 'smtp.yandex.ru'
# EMAIL_HOST_USER = 'info@autister.com'
# EMAIL_HOST_PASSWORD = '******'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# SERVER_EMAIL = EMAIL_HOST_USER
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# For django-allauth authorization throw social networks
# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'vk': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '7292392',
            'secret': 'QKjz1XrjQGhcYUiM7npg',
            'key': ''
        }
    }
}