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
    'ok': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '512000282696',
            'secret': 'CJEBFJJGDIHBABABA',
            'key': 'CJEBFJJGDIHBABABA'
        }
    'facebook':
       {'METHOD': 'oauth2',
        'SCOPE': ['email','public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time'],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'ru_RU',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.4'}
    }
}