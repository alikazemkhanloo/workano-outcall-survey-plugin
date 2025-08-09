from xivo_dao.helpers.db_manager import daosession
from .persistor import OutcallSurveyPersistor
from .search import survey_search

from datetime import timedelta


@daosession
def _persistor(session, tenant_uuids=None):
    return OutcallSurveyPersistor(session, survey_search, tenant_uuids)



def create(outcall_survey):
    return _persistor().create(outcall_survey)


def put(outcall_survey):
    _persistor().put(outcall_survey)


def delete(outcall_survey):
    _persistor().delete(outcall_survey)


def get(outcall_survey_id, tenant_uuids=None):
    return _persistor(tenant_uuids).get_by({'id': outcall_survey_id})


def find(outcall_survey_id, tenant_uuids=None):
    return _persistor(tenant_uuids).find_by({'id': outcall_survey_id})


def find_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).find_by(criteria)


def search(tenant_uuids=None, **parameters):
    return _persistor(tenant_uuids).search(parameters)


def find_all_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).find_all_by(criteria)


def edit(outcall_survey):
    _persistor().edit(outcall_survey)

# def create(queuefeatures):
#     return _persistor().create(queuefeatures)

