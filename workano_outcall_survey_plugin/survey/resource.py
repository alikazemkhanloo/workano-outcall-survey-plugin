import logging

from flask import url_for, request, make_response
from flask_restful import Resource
from wazo_confd.auth import required_acl
from wazo_confd.helpers.restful import ItemResource, ListResource

from .model import SurveyModel, QueueFeaturesModel
from .schema import SurveySchema, QueueFeaturesSchema
import json

logger = logging.getLogger(__name__)


# class SurveyListResource(ListResource):
#     schema = SurveySchema
#     model = SurveyModel

#     def build_headers(self, model):
#         return {'Location': url_for('surveys', uuid=model.id, _external=True)}

#     @required_acl('confd.surveys.read')
#     def get(self):
#         return super().get()

