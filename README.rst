django-action-log
-----------------
.. image:: https://img.shields.io/pypi/dm/django-action-log.svg
    :target:  https://pypi.python.org/pypi/django-action-log/

.. image:: https://img.shields.io/pypi/v/django-action-log.svg
    :target:  https://pypi.python.org/pypi/django-action-log/


Simple and small action logger for django. You can log arbitrary action with username and optional payload that goes with your action.

`django-action-log` is a simple, small, reusable application that provides
support for logging custom actions in django.

You can log arbitrary action with username and optional payload that goes with your action.

Example
-------
from action_log.models import ActionRecord

ActionRecord.objects.create_record(
    'example_action_name',
    username='username or some identifier',
    payload='{"param1": "custom value", "param2": "different value"}'
)
