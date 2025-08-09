import logging

from workano_outcall_survey_plugin.survey.resource import OutcallSurveyItemResource, OutcallSurveyListResource
from workano_outcall_survey_plugin.survey.services import build_outcall_survey_service

from .db import init_db

logger = logging.getLogger(__name__)


class Plugin:
    def load(self, dependencies):
        logger.info('workano survey plugin start loading')
        init_db(
            'postgresql://asterisk:proformatique@localhost/asterisk?application_name=workano-outcall-survey-plugin')
        api = dependencies['api']
        outcall_survey_service= build_outcall_survey_service()
        api.add_resource(
            OutcallSurveyListResource,
            '/outcall-surveys',
            resource_class_args=(outcall_survey_service,)
        )

        api.add_resource(
            OutcallSurveyItemResource,
            '/outcall-surveys/<id>',
            resource_class_args=(outcall_survey_service,)
        )

        logger.info('!!!!!!!!!!!!! workano survey plugin loaded!!!!')
