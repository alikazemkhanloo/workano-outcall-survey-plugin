# -*- coding: utf-8 -*-
# Copyright 2007-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import logging
import re
from wazo_agid.schedule import ScheduleAction, SchedulePeriodBuilder, Schedule, \
    AlwaysOpenedSchedule

import datetime

from xivo_dao import user_dao

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
