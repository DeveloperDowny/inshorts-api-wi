import connexion
import six

from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.login_request import LoginRequest  # noqa: E501
from swagger_server.models.login_response import LoginResponse  # noqa: E501
from swagger_server.models.signup_request import SignupRequest  # noqa: E501
from swagger_server.models.signup_response import SignupResponse  # noqa: E501
from swagger_server import util

from swagger_server.services.auth_service import AuthService


def api_login_post(body):  # noqa: E501
    """Login user

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: LoginResponse
    """
    # if connexion.request.is_json:
    #     body = LoginRequest.from_dict(connexion.request.get_json())  # noqa: E501
    # return 'do some magic!' 

    if not connexion.request.is_json:
        return ErrorResponse(status="Invalid request format", status_code=400), 400
    
    body = LoginRequest.from_dict(connexion.request.get_json())
    user, token = AuthService.login(body.username, body.password)
    if user and token:
        return LoginResponse(status="Login successful", status_code=200, user_id=str(user.id), access_token=token), 200
    else:
        return ErrorResponse(status="Incorrect username/password provided. Please retry", status_code=401), 401



def api_signup_post(body):  # noqa: E501
    """Register a new user

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: SignupResponse
    """
    # if connexion.request.is_json:
    #     body = SignupRequest.from_dict(connexion.request.get_json())  # noqa: E501
    # return 'do some magic!' 

    if not connexion.request.is_json:
        return ErrorResponse(status="Invalid request format", status_code=400), 400
    
    body = SignupRequest.from_dict(connexion.request.get_json())
    try:
        user = AuthService.signup(body.username, body.email, body.password)
        if not user:
            return ErrorResponse(status="Username or email already exists", status_code=400), 400
        return SignupResponse(status="Account successfully created", status_code=200, user_id=str(user.id)), 200
    except ValueError as e:
        return ErrorResponse(status=str(e), status_code=400), 400



