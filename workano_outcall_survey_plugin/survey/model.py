from __future__ import unicode_literals

from sqlalchemy.schema import (
    Column,
    Index,
    ForeignKey,
    PrimaryKeyConstraint,
    UniqueConstraint,
)
from sqlalchemy.types import Integer, String
from xivo_dao.helpers.db_manager import Base, UUIDAsString


from ..db import Base


class SurveyModel(Base):
    __tablename__ = 'plugin_survey'

    id = Column(Integer, nullable=False)
    tenant_uuid = Column(UUIDAsString(36), nullable=False)
    agent_id = Column(String(128), nullable=True)
    agent_number = Column(String(128), nullable=True)
    queue_id = Column(String(128), nullable=True)
    queue_name = Column(String(128), nullable=True)
    queue_number = Column(String(128), nullable=True)
    queue_exten = Column(String(128), nullable=True)
    caller_id = Column(String(128), nullable=True)
    linked_id = Column(String(128), nullable=True)
    call_id = Column(String(128), nullable=True)
    timestamp = Column(String(50), nullable=True)
    rate = Column(String(50), nullable=True)
    vm_message_id = Column(String(50), nullable=True)
    voicemail_id=Column(String(50), nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint('id'), 
    )   
