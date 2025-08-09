from wazo_confd import bus, sysconfd


class OutcallSurveyNotifier:
    def __init__(self, bus, sysconfd):
        self.bus = bus
        self.sysconfd = sysconfd

    def send_sysconfd_handlers(self):
        pass

    def created(self, survey):
        pass

    def edited(self, survey):
        pass

    def deleted(self, survey):
        pass


def build_outcall_survey_notifier():
    return OutcallSurveyNotifier(bus, sysconfd)

