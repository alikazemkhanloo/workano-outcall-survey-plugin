from wazo_confd.helpers.validator import Validator, ValidationGroup


class OutcallSurveyValidator(Validator):
    def validate(self, model):
        return


def build_outcall_survey_validator():
    outcall_survey_validator = OutcallSurveyValidator()
    return ValidationGroup(create=[outcall_survey_validator], edit=[outcall_survey_validator])

