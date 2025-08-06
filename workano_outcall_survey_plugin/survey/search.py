from xivo_dao.resources.utils.search import SearchConfig
from xivo_dao.resources.utils.search import SearchSystem

from .model import SurveyModel

survey_config = SearchConfig(
    table=SurveyModel,
    columns={
        'id': SurveyModel.id,
        'tenant_uuid': SurveyModel.tenant_uuid,
        'queue_id': SurveyModel.queue_id,
    },
    default_sort='id',
)

survey_search = SearchSystem(survey_config)
