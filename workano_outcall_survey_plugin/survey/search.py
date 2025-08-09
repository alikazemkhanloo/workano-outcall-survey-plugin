from xivo_dao.resources.utils.search import SearchConfig
from xivo_dao.resources.utils.search import SearchSystem

from .model import OutcallSurveyModel

outcall_survey_config = SearchConfig(
    table=OutcallSurveyModel,
    columns={
        'id': OutcallSurveyModel.id,
        'tenant_uuid': OutcallSurveyModel.tenant_uuid,
        'users': OutcallSurveyModel.users,
    },
    default_sort='id',
)

outcall_survey_search = SearchSystem(outcall_survey_config)
