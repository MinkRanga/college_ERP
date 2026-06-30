from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import all models here
from app.models.college import College
from app.models.role import Role
from app.models.permission import Permission
from app.models.user import User