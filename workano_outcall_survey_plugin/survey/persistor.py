from xivo_dao.helpers.persistor import BasePersistor
from xivo_dao.resources.utils.search import CriteriaBuilderMixin
from .model import OutcallSurveyModel

class OutcallSurveyPersistor(CriteriaBuilderMixin, BasePersistor):
    _search_table = OutcallSurveyModel

    def __init__(self, session, outcall_survey_search, tenant_uuids=None):
        self.session = session
        self.search_system = outcall_survey_search
        self.tenant_uuids = tenant_uuids

    def _find_query(self, criteria):
        query = self.session.query(OutcallSurveyModel)
        return self.build_criteria(query, criteria)

    def _search_query(self):
        return self.session.query(self.search_system.config.table)


