# -*- coding: utf-8 -*-
# Copyright 2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import logging

from wazo_agid import agid
from wazo_agid.handlers import outcall_survey

logger = logging.getLogger(__name__)


def outcall_survey_log(agi, cursor, args):
    handler = outcall_survey.OutcallSurveyLogHandler(agi, cursor, args)
    handler.execute()


agid.register(outcall_survey_log)
