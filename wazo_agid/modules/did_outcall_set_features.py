# -*- coding: utf-8 -*-
# Copyright 2006-2021 The Wazo Authors
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_agid import agid

def did_outcall_set_features(agi, cursor, args):
    destination_number = agi.get_variable('WAZO_DSTNUM')
    print('destination_number', destination_number)
    if destination_number in ['09122066204', '09104719336']:
        agi.set_variable('WAZO_SURVEY_ENABLE', '1')
    
# Register the AGI handler
agid.register(did_outcall_set_features)
