from marshmallow import fields, pre_load
from wazo_confd.helpers.mallow import BaseSchema


    
class SurveySchema(BaseSchema):
    id = fields.Integer(dump_only=True)
    tenant_uuid = fields.String(dump_only=True)
    agent_id = fields.String(dump_only=True)
    agent_number = fields.String(dump_only=True)
    queue_id = fields.String(dump_only=True)
    queue_name = fields.String(dump_only=True)
    queue_number = fields.String(dump_only=False)
    queue_exten = fields.String(dump_only=False)
    caller_id = fields.String(dump_only=False)
    linked_id = fields.String(dump_only=False) 
    call_id = fields.String(dump_only=False)
    timestamp = fields.String(dump_only=True)
    rate = fields.String(dump_only=True)
    vm_message_id = fields.String()
    voicemail_id = fields.String()



    
class OutcallSurveySchema(BaseSchema):
    id = fields.Int(required=True)
    users = fields.List(fields.String(), required=False)
    enabled = fields.Bool(required=True, missing=False)
    voicemail_threshold = fields.Int(allow_none=True)
    voicemail_id = fields.String(allow_none=True, validate=lambda s: len(s) <= 50)
