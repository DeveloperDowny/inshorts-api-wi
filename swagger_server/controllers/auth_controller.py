import connexion
import six

from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.login_request import LoginRequest  # noqa: E501
from swagger_server.models.login_response import LoginResponse  # noqa: E501
from swagger_server.models.signup_request import SignupRequest  # noqa: E501
from swagger_server.models.signup_response import SignupResponse  # noqa: E501
from swagger_server import util


def api_login_post(body):  # noqa: E501
    """Login user

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: LoginResponse
    """
    if connexion.request.is_json:
        body = LoginRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_signup_post(body):  # noqa: E501
    """Register a new user

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: SignupResponse
    """
    if connexion.request.is_json:
        body = SignupRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
