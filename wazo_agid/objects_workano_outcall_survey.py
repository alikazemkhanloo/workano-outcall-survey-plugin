# -*- coding: utf-8 -*-
# Copyright 2007-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import datetime
import logging

logger = logging.getLogger(__name__)


class DBUpdateException(Exception):
    pass


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



class QueueSurvey(object):
    def __init__(self, agi, cursor, tenant_uuid, agent_id, agent_number, queue_id, queue_name, queue_number,  queue_exten, caller_id, linked_id, call_id, vote_number):
        self.agi = agi
        self.cursor = cursor
        self.tenant_uuid = tenant_uuid
        self.queue_id = queue_id
        self.queue_name = queue_name
        self.queue_number = queue_number
        self.agent_id = agent_id
        self.agent_number = agent_number
        self.linked_id = linked_id
        self.call_id = call_id
        self.queue_exten = queue_exten
        self.caller_id = caller_id
        self.vote_number = vote_number
        ct = datetime.datetime.now()
        timestamp = ct.strftime("%Y-%m-%d %H:%M:%S")

        survey_log_columns = [
            'tenant_uuid', 'agent_id', 'agent_number', 'queue_id', 'queue_name', 'queue_number', 'queue_exten', 'caller_id', 'linked_id', 'call_id', 'timestamp', 'rate'
        ]

        query = "INSERT INTO plugin_survey ({}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(
            ', '.join(survey_log_columns))
        arguments = (self.tenant_uuid, self.agent_id, self.agent_number, self.queue_id,
                     self.queue_name, self.queue_number, self.queue_exten, self.caller_id, self.linked_id, self.call_id, timestamp, self.vote_number)

        self.cursor.execute(query, arguments)  # Corrected from `query` to `execute`

    def save_queue_survey_log_(self):
        pass