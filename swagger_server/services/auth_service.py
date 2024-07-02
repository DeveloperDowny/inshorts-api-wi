from flask_jwt_extended import create_access_token
from datetime import timedelta
from swagger_server.database.database_models import db, User
from passlib.hash import pbkdf2_sha256


class AuthService:
    @staticmethod
    def signup(username, email, password):
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            return None

        hashed_password = pbkdf2_sha256.hash(password)
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return new_user 

    @staticmethod
    def login(username, password):
        user = User.query.filter_by(username=username).first()
        if user and pbkdf2_sha256.verify(password, user.password):
            access_token = create_access_token(identity=user.id)
            return user, access_token
        return None, None