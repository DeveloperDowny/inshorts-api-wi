# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.votes import Votes  # noqa: F401,E501
from swagger_server import util


class Short(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, short_id: str=None, category: str=None, title: str=None, author: str=None, publish_date: datetime=None, content: str=None, actual_content_link: str=None, image: str=None, votes: Votes=None):  # noqa: E501
        """Short - a model defined in Swagger

        :param short_id: The short_id of this Short.  # noqa: E501
        :type short_id: str
        :param category: The category of this Short.  # noqa: E501
        :type category: str
        :param title: The title of this Short.  # noqa: E501
        :type title: str
        :param author: The author of this Short.  # noqa: E501
        :type author: str
        :param publish_date: The publish_date of this Short.  # noqa: E501
        :type publish_date: datetime
        :param content: The content of this Short.  # noqa: E501
        :type content: str
        :param actual_content_link: The actual_content_link of this Short.  # noqa: E501
        :type actual_content_link: str
        :param image: The image of this Short.  # noqa: E501
        :type image: str
        :param votes: The votes of this Short.  # noqa: E501
        :type votes: Votes
        """
        self.swagger_types = {
            'short_id': str,
            'category': str,
            'title': str,
            'author': str,
            'publish_date': datetime,
            'content': str,
            'actual_content_link': str,
            'image': str,
            'votes': Votes
        }

        self.attribute_map = {
            'short_id': 'short_id',
            'category': 'category',
            'title': 'title',
            'author': 'author',
            'publish_date': 'publish_date',
            'content': 'content',
            'actual_content_link': 'actual_content_link',
            'image': 'image',
            'votes': 'votes'
        }
        self._short_id = short_id
        self._category = category
        self._title = title
        self._author = author
        self._publish_date = publish_date
        self._content = content
        self._actual_content_link = actual_content_link
        self._image = image
        self._votes = votes

    @classmethod
    def from_dict(cls, dikt) -> 'Short':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Short of this Short.  # noqa: E501
        :rtype: Short
        """
        return util.deserialize_model(dikt, cls)

    @property
    def short_id(self) -> str:
        """Gets the short_id of this Short.


        :return: The short_id of this Short.
        :rtype: str
        """
        return self._short_id

    @short_id.setter
    def short_id(self, short_id: str):
        """Sets the short_id of this Short.


        :param short_id: The short_id of this Short.
        :type short_id: str
        """

        self._short_id = short_id

    @property
    def category(self) -> str:
        """Gets the category of this Short.


        :return: The category of this Short.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category: str):
        """Sets the category of this Short.


        :param category: The category of this Short.
        :type category: str
        """

        self._category = category

    @property
    def title(self) -> str:
        """Gets the title of this Short.


        :return: The title of this Short.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this Short.


        :param title: The title of this Short.
        :type title: str
        """

        self._title = title

    @property
    def author(self) -> str:
        """Gets the author of this Short.


        :return: The author of this Short.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author: str):
        """Sets the author of this Short.


        :param author: The author of this Short.
        :type author: str
        """

        self._author = author

    @property
    def publish_date(self) -> datetime:
        """Gets the publish_date of this Short.


        :return: The publish_date of this Short.
        :rtype: datetime
        """
        return self._publish_date

    @publish_date.setter
    def publish_date(self, publish_date: datetime):
        """Sets the publish_date of this Short.


        :param publish_date: The publish_date of this Short.
        :type publish_date: datetime
        """

        self._publish_date = publish_date

    @property
    def content(self) -> str:
        """Gets the content of this Short.


        :return: The content of this Short.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content: str):
        """Sets the content of this Short.


        :param content: The content of this Short.
        :type content: str
        """

        self._content = content

    @property
    def actual_content_link(self) -> str:
        """Gets the actual_content_link of this Short.


        :return: The actual_content_link of this Short.
        :rtype: str
        """
        return self._actual_content_link

    @actual_content_link.setter
    def actual_content_link(self, actual_content_link: str):
        """Sets the actual_content_link of this Short.


        :param actual_content_link: The actual_content_link of this Short.
        :type actual_content_link: str
        """

        self._actual_content_link = actual_content_link

    @property
    def image(self) -> str:
        """Gets the image of this Short.


        :return: The image of this Short.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image: str):
        """Sets the image of this Short.


        :param image: The image of this Short.
        :type image: str
        """

        self._image = image

    @property
    def votes(self) -> Votes:
        """Gets the votes of this Short.


        :return: The votes of this Short.
        :rtype: Votes
        """
        return self._votes

    @votes.setter
    def votes(self, votes: Votes):
        """Sets the votes of this Short.


        :param votes: The votes of this Short.
        :type votes: Votes
        """

        self._votes = votes
