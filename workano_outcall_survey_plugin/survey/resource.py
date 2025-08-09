import logging

from flask import url_for, request, make_response
from flask_restful import Resource
from wazo_confd.auth import required_acl
from wazo_confd.helpers.restful import ItemResource, ListResource

from .model import OutcallSurveyModel
from .schema import OutcallSurveySchema
import json

logger = logging.getLogger(__name__)


class OutcallSurveyListResource(ListResource):
    schema = OutcallSurveySchema
    model = OutcallSurveyModel

    def build_headers(self, model):
        return {'Location': url_for('surveys', uuid=model.id, _external=True)}

    @required_acl('confd.outcall-surveys.read')
    def get(self):
        return super().get()

    @required_acl('confd.outcall-surveys.create')
    def post(self):
        return super().post()
    




class OutcallSurveyItemResource(ItemResource):
    schema = OutcallSurveySchema
    model = OutcallSurveyModel

    def build_headers(self, model):
        return {'Location': url_for('surveys', uuid=model.id, _external=True)}

    @required_acl('confd.outcall-surveys.read')
    def get(self, id):
        return super().get(id)

    @required_acl('confd.outcall-surveys.update')
    def put(self, id):
        return super().put(id)

    @required_acl('confd.outcall-surveys.delete')
    def delete(self, id):
        return super().delete(id)
    

