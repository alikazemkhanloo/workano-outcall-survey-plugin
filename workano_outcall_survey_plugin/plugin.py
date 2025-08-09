import logging

from workano_outcall_survey_plugin.survey.resource import OutcallSurveyItemResource, OutcallSurveyListResource

from .db import init_db

logger = logging.getLogger(__name__)


class Plugin:
    def load(self, dependencies):
        logger.info('workano survey plugin start loading')
        init_db(
            'postgresql://asterisk:proformatique@localhost/asterisk?application_name=workano-outcall-survey-plugin')
        api = dependencies['api']

        api.add_resource(
            OutcallSurveyListResource,
            '/outcall-survey',
            # resource_class_args=(queuefeature_service,)
        )

        api.add_resource(
            OutcallSurveyItemResource,
            '/outcall-survey/<id>',
            # resource_class_args=(queuefeature_service,)
        )

        logger.info('!!!!!!!!!!!!! workano survey plugin loaded!!!!')
