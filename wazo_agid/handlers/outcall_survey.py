# -*- coding: utf-8 -*-
# Copyright 2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import os
import re
import logging
import glob

from wazo_agid import objects_workano_outcall_survey
from wazo_agid.handlers import handler

logger = logging.getLogger(__name__)

AGENT_CHANNEL_RE = re.compile(r'^Local/id-(\d+)@agentcallback-[a-f0-9]+;1$')
RECORDINGS_DIRECTORY = '/var/spool/asterisk/voicemail'

class OutcallSurveyHandler(handler.Handler):
    def execute(self):
        user_uuid = self._agi.get_variable('WAZO_USERUUID')
        call_direction = self._agi.get_variable('WAZO_CALL_DIRECTION') #  == outbound
        if call_direction != 'outbound':
            return
        outcall_survey = objects_workano_outcall_survey.OutcallSurvey(self._cursor, user_uuid)
        print('outcall_survey ', outcall_survey.voicemail_mailbox,
                outcall_survey.voicemail_id,
                outcall_survey.voicemail_context,
                outcall_survey.voicemail_threshold)
        if outcall_survey.enabled:
            self._agi.set_variable('WAZO_SURVEY_ENABLE', '1')
            if outcall_survey.voicemail_id:
                print('outcall_survey.voicemail_id', outcall_survey.voicemail_id)
                self._agi.set_variable('OUTCALL_SURVEY_VOICEMAIL_MAILBOX', outcall_survey.voicemail_mailbox)
                self._agi.set_variable('OUTCALL_SURVEY_VOICEMAIL_ID', outcall_survey.voicemail_id)
                self._agi.set_variable('OUTCALL_SURVEY_VOICEMAIL_CONTEXT', outcall_survey.voicemail_context)
                self._agi.set_variable('OUTCALL_SURVEY_VOICEMAIL_THRESHOLD', outcall_survey.voicemail_threshold)
                


class OutcallSurveyVoiceMessageHandler(handler.Handler):
    def execute(self):
        destination_number = self._agi.get_variable('WAZO_DSTNUM')
        linked_id = self._agi.get_variable('CHANNEL(linkedid)') or 'default_linked_id'
        mailbox = self._agi.get_variable('OUTCALL_SURVEY_VOICEMAIL_MAILBOX')
        voicemail_id = self._agi.get_variable('OUTCALL_SURVEY_VOICEMAIL_ID')
        vm_context = self._agi.get_variable('OUTCALL_SURVEY_VOICEMAIL_CONTEXT')
        inbox_path = os.path.join(RECORDINGS_DIRECTORY, vm_context, mailbox, 'INBOX')
        self._agi.verbose(f'inbox_path {inbox_path}, LINKEDID: {linked_id}')
        if not os.path.exists(inbox_path):
            self._agi.verbose(f"INBOX path does not exist: {inbox_path}")
            return
        txt_files = glob.glob(os.path.join(inbox_path, 'msg*.txt'))

        # Sort files by last modified time (newest first)
        txt_files.sort(key=lambda f: os.path.getmtime(f), reverse=True)

        # Limit to last 5 files
        last_txt_files = txt_files[:5]
        self._agi.verbose(f'txt_files: {last_txt_files}')

        message_id = None
        for txt_file in last_txt_files:
            with open(txt_file, 'r') as f:
                content = f.read()
                match = re.search(r'callerid=".*?"\s*<(\d+)>', content)
                if match:
                    file_caller_id = match.group(1)
                    if destination_number in file_caller_id:
                        msgid_match = re.search(r'^msg_id=(.+)', content, re.MULTILINE)
                        if msgid_match:
                            msg_id = msgid_match.group(1).strip()
                            self._agi.verbose(f"[MATCH] Found msg_id: {msg_id} for caller ID {destination_number}")
                            print(f"[MATCH] Found msg_id: {msg_id} for caller ID {destination_number}")
                            message_id = msg_id
                            objects_workano_outcall_survey.OutcallSurveyUpdateMessageId(self._cursor, linked_id, message_id, voicemail_id)
                            return None
                        else:
                            self._agi.verbose('msgid not matched')
                    else:
                        self._agi.verbose('caller_id not matched')
                else:
                    self._agi.verbose('caller id not found')
                
        self._agi.verbose("[INFO] No matching voicemail msg_id found in last 5 messages.")
        return None


class OutcallSurveyLogHandler(handler.Handler):
    def execute(self):
        vote_number = self._agi.get_variable('WAZO_VOTE_NUMBER')
        self._agi.verbose('AGI: vote_number {}'.format(vote_number))

        if vote_number:
            tenant_uuid = self._agi.get_variable('WAZO_TENANT_UUID') or 'default_tenant_uuid'
            destination_number = self._agi.get_variable('WAZO_DSTNUM') or 'default_caller_id'

            call_id = self._agi.get_variable('WAZO_SIP_CALL_ID') or 'default_call_id'
            linked_id = self._agi.get_variable('CHANNEL(linkedid)') or 'default_linked_id'

            objects_workano_outcall_survey.QueueSurvey(self._agi, self._cursor, tenant_uuid, destination_number,
                                        linked_id, call_id, vote_number)
            logger.debug('handler saved ')
