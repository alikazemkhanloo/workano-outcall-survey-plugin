from xivo_dao.helpers.db_manager import daosession
from .persistor import SurveyPersistor, QueueFeatursPersistor
from .search import survey_search, queuefeature_search

from datetime import timedelta


@daosession
def _persistor(session, tenant_uuids=None):
    return SurveyPersistor(session, survey_search, tenant_uuids)



# def create(queuefeatures):
#     return _persistor().create(queuefeatures)

