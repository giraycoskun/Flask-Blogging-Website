"""_summary_

Returns:
    _type_: _description_
"""

from uuid import UUID, uuid4

from sqlalchemy import event
from sqlalchemy_utils import UUIDType
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

from service.auth import login_manager
from repository import db


class User(UserMixin, db.Model):
    """User ORM Model

    Args:
        UserMixin (_type_): _description_
        db (_type_): _description_

    Returns:
        _type_: _description_
    """
    __tablename__ = 'user'

    id = db.Column('id', UUIDType(binary=False),
                   default=uuid4, primary_key=True)
    username = db.Column('username', db.String(256),
                         nullable=False, unique=True)
    name = db.Column('name', db.String(256), nullable=False)
    role = db.Column('role', db.Integer, nullable=False)
    """ROLE
    USER=0
    BLOGGER=1
    ADMIN=2
    """
    password_hash = db.Column('password_hash', db.String(128), nullable=False)

    def __repr__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return f"User {self.username}"

    @property
    def is_admin(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.role == 2

    def verify_password(self, password):
        """_summary_

        Args:
            password (_type_): _description_

        Returns:
            _type_: _description_
        """
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    """_summary_

    Args:
        user_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        user_id = UUID(user_id)
        return User.query.get(user_id)
    except:
        return None


@event.listens_for(User.password_hash, 'set', retval=True)
def hash_user_password(target, value, oldvalue, initiator):
    """_summary_

    Args:
        target (_type_): _description_
        value (_type_): _description_
        oldvalue (_type_): _description_
        initiator (_type_): _description_

    Returns:
        _type_: _description_
    """
    if value != oldvalue:
        return generate_password_hash(value)
    return value


def get_user_by_id(id):
    """_summary_

    Args:
        id (_type_): _description_

    Returns:
        _type_: _description_
    """
    return User.query.get(id).first()


def get_user_by_username(username):
    """_summary_

    Args:
        username (_type_): _description_

    Returns:
        _type_: _description_
    """
    return User.query.filter_by(username=username).first()


def create_user(username, name, role, password):
    """_summary_

    Args:
        username (_type_): _description_
        name (_type_): _description_
        role (_type_): _description_
        password (_type_): _description_
    """
    user = User(username=username, name=name,
                role=role, password_hash=password)
    db.session.add(user)
    db.session.commit()


def create_admin_user(app):
    """_summary_

    Args:
        app (_type_): _description_
    """
    with app.app_context():
        create_user(username='admin', name='flask-blog', role=2,
                    password=app.config['ADMIN_USER_PASSWORD'])
