from wazo_confd.helpers.resource import CRUDService

from . import dao
from .notifier import build_survey_notifier
from .validator import build_survey_validator


class SurveyService(CRUDService):
    pass
    # def get_all_surveys(self, tenant_uuid, queue_id):
    #     return dao.get_all_surveys(tenant_uuid, queue_id)


def build_survey_service():
    return SurveyService(dao, build_survey_validator(), build_survey_notifier())

