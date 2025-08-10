# -*- coding: utf-8 -*-
# Copyright 2007-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import datetime
import logging

logger = logging.getLogger(__name__)


class DBUpdateException(Exception):
    pass


class OutcallSurveyFeature(object):
    def __init__(self, cursor, user_uuid):
        self.cursor = cursor
        self.user_uuid = user_uuid
        self.enabled = False
        self.voicemail_id = None
        query = """
            select voicemail_id, id, users, enabled, voicemail_threshold from plugin_outcall_survey where %s = ANY(users);
        """
        arguments = (user_uuid,)
        self.cursor.execute(query, arguments)
        res = self.cursor.fetchone()
        voicemail_res = None
        self.voicemail_mailbox = None
        self.voicemail_context = None
        self.voicemail_threshold = None
        if not res: 
            return
        if voicemail_id := res['voicemail_id']:
            self.voicemail_id = voicemail_id
            voicemail_query = "select context, mailbox from voicemail where uniqueid=%s"
            voicemail_arguments = (voicemail_id,)
            self.cursor.execute(voicemail_query, voicemail_arguments)  # Execute the query
            voicemail_res = self.cursor.fetchone()  # Fetch one result

        self.enabled = res['enabled']
        self.voicemail_id = res['voicemail_id']
        self.voicemail_threshold = res['voicemail_threshold']
        if voicemail_res:
            self.voicemail_mailbox = voicemail_res['mailbox']
            self.voicemail_context = voicemail_res['context']
        

class OutcallSurveyUpdateMessageId(object):
    def __init__(self, cursor, linked_id, message_id, voicemail_id):
        self.cursor = cursor

        self.linked_id = linked_id
        self.message_id = message_id
        query = """
            UPDATE plugin_survey
            SET vm_message_id = %s,
                voicemail_id = %s
            WHERE linked_id = %s;
        """
        arguments = (message_id, voicemail_id, linked_id)
        self.cursor.execute(query, arguments)



class OutcallSurveyPersist(object):
    def __init__(self, agi, cursor, tenant_uuid, destination_number, linked_id, call_id, vote_number):
        self.agi = agi
        self.cursor = cursor
        self.tenant_uuid = tenant_uuid
        self.linked_id = linked_id
        self.call_id = call_id
        self.destination_number = destination_number
        self.vote_number = vote_number
        ct = datetime.datetime.now()
        timestamp = ct.strftime("%Y-%m-%d %H:%M:%S")

        survey_log_columns = [
            'tenant_uuid', 'caller_id', 'linked_id', 'call_id', 'timestamp', 'rate', 'type'
        ]

        query = "INSERT INTO plugin_survey ({}) VALUES (%s, %s, %s, %s, %s, %s, 'outcall')".format(
            ', '.join(survey_log_columns))
        arguments = (self.tenant_uuid, self.destination_number, self.linked_id, self.call_id, timestamp, self.vote_number)

        self.cursor.execute(query, arguments)

    def save_queue_survey_log_(self):
        pass