from xivo_dao.resources.utils.search import SearchConfig
from xivo_dao.resources.utils.search import SearchSystem

from .model import OutcallSurveyModel

survey_config = SearchConfig(
    table=OutcallSurveyModel,
    columns={
        'id': OutcallSurveyModel.id,
        'tenant_uuid': OutcallSurveyModel.tenant_uuid,
        'queue_id': OutcallSurveyModel.queue_id,
    },
    default_sort='id',
)

survey_search = SearchSystem(survey_config)
