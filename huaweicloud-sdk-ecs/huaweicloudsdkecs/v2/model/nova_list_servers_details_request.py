# coding: utf-8

import pprint
import re

import six


class NovaListServersDetailsRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'open_stack_api_version': 'str',
        'changes_since': 'str',
        'ip': 'str',
        'image': 'str',
        'flavor': 'str',
        'name': 'str',
        'status': 'str',
        'limit': 'int',
        'marker': 'str',
        'tags': 'str',
        'not_tags': 'str',
        'reservation_id': 'str',
        'sort_key': 'str'
    }

    attribute_map = {
        'open_stack_api_version': 'OpenStack-API-Version',
        'changes_since': 'changes-since',
        'ip': 'ip',
        'image': 'image',
        'flavor': 'flavor',
        'name': 'name',
        'status': 'status',
        'limit': 'limit',
        'marker': 'marker',
        'tags': 'tags',
        'not_tags': 'not-tags',
        'reservation_id': 'reservation_id',
        'sort_key': 'sort_key'
    }

    def __init__(self, open_stack_api_version='compute 2.60', changes_since=None, ip=None, image=None, flavor=None, name=None, status=None, limit=25, marker=None, tags=None, not_tags=None, reservation_id=None, sort_key='created_at'):  # noqa: E501
        """NovaListServersDetailsRequest - a model defined in huaweicloud sdk"""

        self._open_stack_api_version = None
        self._changes_since = None
        self._ip = None
        self._image = None
        self._flavor = None
        self._name = None
        self._status = None
        self._limit = None
        self._marker = None
        self._tags = None
        self._not_tags = None
        self._reservation_id = None
        self._sort_key = None
        self.discriminator = None

        if open_stack_api_version is not None:
            self.open_stack_api_version = open_stack_api_version
        if changes_since is not None:
            self.changes_since = changes_since
        if ip is not None:
            self.ip = ip
        if image is not None:
            self.image = image
        if flavor is not None:
            self.flavor = flavor
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if tags is not None:
            self.tags = tags
        if not_tags is not None:
            self.not_tags = not_tags
        if reservation_id is not None:
            self.reservation_id = reservation_id
        if sort_key is not None:
            self.sort_key = sort_key

    @property
    def open_stack_api_version(self):
        """Gets the open_stack_api_version of this NovaListServersDetailsRequest.


        :return: The open_stack_api_version of this NovaListServersDetailsRequest.
        :rtype: str
        """
        return self._open_stack_api_version

    @open_stack_api_version.setter
    def open_stack_api_version(self, open_stack_api_version):
        """Sets the open_stack_api_version of this NovaListServersDetailsRequest.


        :param open_stack_api_version: The open_stack_api_version of this NovaListServersDetailsRequest.
        :type: str
        """
        self._open_stack_api_version = open_stack_api_version

    @property
    def changes_since(self):
        """Gets the changes_since of this NovaListServersDetailsRequest.


        :return: The changes_since of this NovaListServersDetailsRequest.
        :rtype: str
        """
        return self._changes_since

    @changes_since.setter
    def changes_since(self, changes_since):
        """Sets the changes_since of this NovaListServersDetailsRequest.


        :param changes_since: The changes_since of this NovaListServersDetailsRequest.
        :type: str
        """
        self._changes_since = changes_since

    @property
    def ip(self):
        """Gets the ip of this NovaListServersDetailsRequest.


        :return: The ip of this NovaListServersDetailsRequest.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this NovaListServersDetailsRequest.


        :param ip: The ip of this NovaListServersDetailsRequest.
        :type: str
        """
        self._ip = ip

    @property
    def image(self):
        """Gets the image of this NovaListServersDetailsRequest.


        :return: The image of this NovaListServersDetailsRequest.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this NovaListServersDetailsRequest.


        :param image: The image of this NovaListServersDetailsRequest.
        :type: str
        """
        self._image = image

    @property
    def flavor(self):
        """Gets the flavor of this NovaListServersDetailsRequest.


        :return: The flavor of this NovaListServersDetailsRequest.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this NovaListServersDetailsRequest.


        :param flavor: The flavor of this NovaListServersDetailsRequest.
        :type: str
        """
        self._flavor = flavor

    @property
    def name(self):
        """Gets the name of this NovaListServersDetailsRequest.


        :return: The name of this NovaListServersDetailsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NovaListServersDetailsRequest.


        :param name: The name of this NovaListServersDetailsRequest.
        :type: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this NovaListServersDetailsRequest.


        :return: The status of this NovaListServersDetailsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NovaListServersDetailsRequest.


        :param status: The status of this NovaListServersDetailsRequest.
        :type: str
        """
        self._status = status

    @property
    def limit(self):
        """Gets the limit of this NovaListServersDetailsRequest.


        :return: The limit of this NovaListServersDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this NovaListServersDetailsRequest.


        :param limit: The limit of this NovaListServersDetailsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this NovaListServersDetailsRequest.


        :return: The marker of this NovaListServersDetailsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this NovaListServersDetailsRequest.


        :param marker: The marker of this NovaListServersDetailsRequest.
        :type: str
        """
        self._marker = marker

    @property
    def tags(self):
        """Gets the tags of this NovaListServersDetailsRequest.


        :return: The tags of this NovaListServersDetailsRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this NovaListServersDetailsRequest.


        :param tags: The tags of this NovaListServersDetailsRequest.
        :type: str
        """
        self._tags = tags

    @property
    def not_tags(self):
        """Gets the not_tags of this NovaListServersDetailsRequest.


        :return: The not_tags of this NovaListServersDetailsRequest.
        :rtype: str
        """
        return self._not_tags

    @not_tags.setter
    def not_tags(self, not_tags):
        """Sets the not_tags of this NovaListServersDetailsRequest.


        :param not_tags: The not_tags of this NovaListServersDetailsRequest.
        :type: str
        """
        self._not_tags = not_tags

    @property
    def reservation_id(self):
        """Gets the reservation_id of this NovaListServersDetailsRequest.


        :return: The reservation_id of this NovaListServersDetailsRequest.
        :rtype: str
        """
        return self._reservation_id

    @reservation_id.setter
    def reservation_id(self, reservation_id):
        """Sets the reservation_id of this NovaListServersDetailsRequest.


        :param reservation_id: The reservation_id of this NovaListServersDetailsRequest.
        :type: str
        """
        self._reservation_id = reservation_id

    @property
    def sort_key(self):
        """Gets the sort_key of this NovaListServersDetailsRequest.


        :return: The sort_key of this NovaListServersDetailsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this NovaListServersDetailsRequest.


        :param sort_key: The sort_key of this NovaListServersDetailsRequest.
        :type: str
        """
        self._sort_key = sort_key

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NovaListServersDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other