# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.login_request import LoginRequest  # noqa: E501
from swagger_server.models.login_response import LoginResponse  # noqa: E501
from swagger_server.models.signup_request import SignupRequest  # noqa: E501
from swagger_server.models.signup_response import SignupResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAuthController(BaseTestCase):
    """AuthController integration test stubs"""

    def test_api_login_post(self):
        """Test case for api_login_post

        Login user
        """
        body = LoginRequest()
        response = self.client.open(
            '/v1/api/login',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_signup_post(self):
        """Test case for api_signup_post

        Register a new user
        """
        body = SignupRequest()
        response = self.client.open(
            '/v1/api/signup',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
