# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.create_short_request import CreateShortRequest  # noqa: E501
from swagger_server.models.create_short_response import CreateShortResponse  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.filter_params import FilterParams  # noqa: E501
from swagger_server.models.filtered_short import FilteredShort  # noqa: E501
from swagger_server.models.search_params import SearchParams  # noqa: E501
from swagger_server.models.short import Short  # noqa: E501
from swagger_server.test import BaseTestCase


class TestShortsController(BaseTestCase):
    """ShortsController integration test stubs"""

    def test_api_shorts_create_post(self):
        """Test case for api_shorts_create_post

        Add a new short
        """
        body = CreateShortRequest()
        response = self.client.open(
            '/v1/api/shorts/create',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_shorts_feed_get(self):
        """Test case for api_shorts_feed_get

        Get shorts feed
        """
        response = self.client.open(
            '/v1/api/shorts/feed',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_shorts_filter_get(self):
        """Test case for api_shorts_filter_get

        Get filtered shorts feed
        """
        query_string = [('filter', FilterParams()),
                        ('search', SearchParams())]
        response = self.client.open(
            '/v1/api/shorts/filter',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
