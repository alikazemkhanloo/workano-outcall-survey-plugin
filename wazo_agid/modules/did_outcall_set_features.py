# -*- coding: utf-8 -*-
# Copyright 2006-2021 The Wazo Authors
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_agid import agid, objects_workano_outcall_survey

def did_outcall_set_features(agi, cursor, args):
    destination_id = agi.get_variable('WAZO_DSTID')
    if destination_id =='09104719336':
        agi.set_variable('WAZO_SURVEY_ENABLE', '1')
    
# Register the AGI handler
agid.register(did_outcall_set_features)
