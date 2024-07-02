# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Votes(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, upvote: int=None, downvote: int=None):  # noqa: E501
        """Votes - a model defined in Swagger

        :param upvote: The upvote of this Votes.  # noqa: E501
        :type upvote: int
        :param downvote: The downvote of this Votes.  # noqa: E501
        :type downvote: int
        """
        self.swagger_types = {
            'upvote': int,
            'downvote': int
        }

        self.attribute_map = {
            'upvote': 'upvote',
            'downvote': 'downvote'
        }
        self._upvote = upvote
        self._downvote = downvote

    @classmethod
    def from_dict(cls, dikt) -> 'Votes':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Votes of this Votes.  # noqa: E501
        :rtype: Votes
        """
        return util.deserialize_model(dikt, cls)

    @property
    def upvote(self) -> int:
        """Gets the upvote of this Votes.


        :return: The upvote of this Votes.
        :rtype: int
        """
        return self._upvote

    @upvote.setter
    def upvote(self, upvote: int):
        """Sets the upvote of this Votes.


        :param upvote: The upvote of this Votes.
        :type upvote: int
        """

        self._upvote = upvote

    @property
    def downvote(self) -> int:
        """Gets the downvote of this Votes.


        :return: The downvote of this Votes.
        :rtype: int
        """
        return self._downvote

    @downvote.setter
    def downvote(self, downvote: int):
        """Sets the downvote of this Votes.


        :param downvote: The downvote of this Votes.
        :type downvote: int
        """

        self._downvote = downvote
