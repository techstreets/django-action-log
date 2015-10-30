# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.db import models


class ActionType(models.Model):
    """This define type of action for action log record."""

    name = models.CharField(
        max_length=100, blank=False, null=False, unique=True
    )
    description = models.CharField(
        max_length=255, blank=True, null=False
    )
    enabled = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.enabled, )

    class Meta:
        app_label = 'action_log'
        db_table = 'action_log__action_type'


class ActionRecordQuerySet(models.QuerySet):
    """Create record to describe performed action at a given time.

    For example this can be user logged in or performed some action
    like search, activate option, changed password ...

    We will use simple string for user identifier. This is
    generally an username for auth application but we don't user
    user object to prevent relations with other apps! Also, this is
    not a mandatory param since there are actions that don't have
    anything to do with user. Those are system action like cron jobs
    or sending promotions to users ...

    If there is no action with provided name, it will be created.
    It will be enabled by default to prevent losing data.

    """

    def create_record(self, action_name, username=None, payload=None):
        """Create action record of provided action type.
        @param:action_name is string of action type name
        @param:username username of a user performing the action
        @param:payload this is optional additional data for action

        """
        action_type, created = ActionType.objects.get_or_create(
            name=action_name
        )
        # if this is a new action, enable it by default
        if created:
            action_type.enabled = True
            action_type.save()
        # only create record for enabled actions
        if not action_type.enabled:
            return None
        if payload is not None:
            try:
                payload = json.dumps(payload)
            except Exception:
                payload = None
        return self.create(
            action_type=action_type, username=username, payload=payload
        )


class ActionRecord(models.Model):
    """This is action log record."""

    action_type = models.ForeignKey(ActionType, blank=False, null=False)
    username = models.CharField(max_length=50, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    payload = models.TextField(blank=True, null=True, default=None)

    objects = ActionRecordQuerySet.as_manager()

    def __unicode__(self):
        return '%s by %s@%s' % (
            self.action_type, self.username, self.date_created,
        )

    class Meta:
        app_label = 'action_log'
        db_table = 'action_log__action_record'
