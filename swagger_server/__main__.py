import connexion
from swagger_server import encoder


# custom
from flask_jwt_extended import JWTManager
from swagger_server.database.database_models import db
from datetime import timedelta
import os

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')


    # Configure SQLAlchemy to use database
    username = os.getenv('DB_USERNAME', 'username')
    password = os.getenv('DB_PASSWORD', 'password')
    hostname = os.getenv('DB_HOST', 'localhost')
    port = os.getenv('DB_PORT', '5432')
    database_name = os.getenv('DB_NAME', 'inshorts')


    app.app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{username}:{password}@{hostname}/{database_name}' # MySQL
    # app.app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{username}:{password}@{hostname}:{port}/{database_name}' # PostgreSQL

    # SQLite
    # app.app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///library_management.db'

    app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Configure JWT
    app.app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'your-secret-key')
    app.app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

    # Initialize extensions
    db.init_app(app.app)
    with app.app.app_context():
        db.create_all()
    jwt = JWTManager(app.app)


    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Swagger Petstore'}, pythonic_params=True)
    # app.run(port=os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=os.getenv('PORT', 8080))


if __name__ == '__main__':
    main()
