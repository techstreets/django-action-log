from django.conf import settings


DEFAULTS = {
    'ACTION_LOG_QUERY_LIMIT': 20,
    'ACTION_LOG_ALOWED_ACTIONS': (),
    # 'ACTION_LOG_ALOWED_ACTIONS': ('', ),
    'ACTION_LOG_ALOWED_FIELDS': (
        'action',
        'date_created',
        'date_created_ISO8601'
    ),
    'ACTION_LOG_ADMIN_QUERY_LIMIT': 0,
}

for name, value in DEFAULTS.items():
    if not hasattr(settings, name):
        setattr(settings, name, value)
