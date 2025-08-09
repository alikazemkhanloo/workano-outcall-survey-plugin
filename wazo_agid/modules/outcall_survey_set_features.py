# -*- coding: utf-8 -*-
# Copyright 2006-2021 The Wazo Authors
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_agid import agid
from wazo_agid.handlers.outcall_survey import OutcallSurveyHandler

def outcall_survey_set_features(agi, cursor, args):
    handler = OutcallSurveyHandler(agi, cursor, args)
    handler.execute()
    
# Register the AGI handler
agid.register(outcall_survey_set_features)
