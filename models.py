from database import Base
from sqlalchemy import Column, ForeignKey, Integer, DateTime, String, Enum, Text, Boolean, TypeDecorator, cast, Date, LargeBinary, Float, literal
from citext import CIText
import datetime
import enum
import uuid

# Define enum types
user_gender = Enum('male', 'female', 'other', name='user_gender')
user_status = Enum('active', 'inactive', name='user_status')
message_type = Enum('text', 'video', 'image', 'document', 'audio', name='message_type')


class Users(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4(), unique=True, nullable=False)
    email = Column(CIText, unique=True, nullable=False)
    phone = Column(String(50), unique=True, nullable=False)
    full_name = Column(String(100))
    gender = Column(user_gender)
    date_of_birth = Column(Date)
    password = Column(LargeBinary)
    address = Column(String)
    status = Column(user_status, default='inactive', nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id
        

class Messages(Base):
    __tablename__ = 'messages'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4(), unique=True, nullable=False)
    body = Column(Text)
    created_by = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    type = Column(message_type, default='text', nullable=False)
    location = Column(String, nullable=False)
    CreatedByRelation = relationship('Users', foreign_keys=created_by)
    
    def __repr__(self):
        return '<Message %r>' % self.id
