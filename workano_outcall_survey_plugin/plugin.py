import logging

from .survey.resource import SurveyListResource, SurveyAgentItemResource, SurveyQueueItemResource, \
    SurveyQueueAverageItemResource, SurveyAgentAverageItemResource, QueueFeaturesListResource, QueueFeaturesItemResource, \
    SurveyAllAgentAverageItemResource, SurveyAllQueueAverageItemResource, SurveyAgentInQueueAverageItemResource, SurveyAllAgentsInQueueAverageItemResource
from .survey.services import build_survey_service, build_queuefeature_service
from .db import init_db

logger = logging.getLogger(__name__)


class Plugin:
    def load(self, dependencies):
        logger.info('workano survey plugin start loading')
        # init_db(
        #     'postgresql://asterisk:proformatique@localhost/asterisk?application_name=wazo-survey-plugin')
        api = dependencies['api']

        # api.add_resource(
        #     QueueFeaturesItemResource,
        #     '/queue-features/<int:uuid>',
        #     resource_class_args=(queuefeature_service,)
        # )

        logger.info('!!!!!!!!!!!!! workano survey plugin loaded!!!!')
