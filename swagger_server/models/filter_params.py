# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class FilterParams(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, category: str=None, publish_date: datetime=None, upvote: int=None):  # noqa: E501
        """FilterParams - a model defined in Swagger

        :param category: The category of this FilterParams.  # noqa: E501
        :type category: str
        :param publish_date: The publish_date of this FilterParams.  # noqa: E501
        :type publish_date: datetime
        :param upvote: The upvote of this FilterParams.  # noqa: E501
        :type upvote: int
        """
        self.swagger_types = {
            'category': str,
            'publish_date': datetime,
            'upvote': int
        }

        self.attribute_map = {
            'category': 'category',
            'publish_date': 'publish_date',
            'upvote': 'upvote'
        }
        self._category = category
        self._publish_date = publish_date
        self._upvote = upvote

    @classmethod
    def from_dict(cls, dikt) -> 'FilterParams':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FilterParams of this FilterParams.  # noqa: E501
        :rtype: FilterParams
        """
        return util.deserialize_model(dikt, cls)

    @property
    def category(self) -> str:
        """Gets the category of this FilterParams.


        :return: The category of this FilterParams.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category: str):
        """Sets the category of this FilterParams.


        :param category: The category of this FilterParams.
        :type category: str
        """

        self._category = category

    @property
    def publish_date(self) -> datetime:
        """Gets the publish_date of this FilterParams.


        :return: The publish_date of this FilterParams.
        :rtype: datetime
        """
        return self._publish_date

    @publish_date.setter
    def publish_date(self, publish_date: datetime):
        """Sets the publish_date of this FilterParams.


        :param publish_date: The publish_date of this FilterParams.
        :type publish_date: datetime
        """

        self._publish_date = publish_date

    @property
    def upvote(self) -> int:
        """Gets the upvote of this FilterParams.


        :return: The upvote of this FilterParams.
        :rtype: int
        """
        return self._upvote

    @upvote.setter
    def upvote(self, upvote: int):
        """Sets the upvote of this FilterParams.


        :param upvote: The upvote of this FilterParams.
        :type upvote: int
        """

        self._upvote = upvote
