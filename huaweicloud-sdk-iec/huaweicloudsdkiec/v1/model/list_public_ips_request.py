# coding: utf-8

import pprint
import re

import six





class ListPublicIpsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'site_id': 'str',
        'port_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'site_id': 'site_id',
        'port_id': 'port_id'
    }

    def __init__(self, limit=None, offset=None, site_id=None, port_id=None):
        """ListPublicIpsRequest - a model defined in huaweicloud sdk"""
        
        

        self._limit = None
        self._offset = None
        self._site_id = None
        self._port_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if site_id is not None:
            self.site_id = site_id
        if port_id is not None:
            self.port_id = port_id

    @property
    def limit(self):
        """Gets the limit of this ListPublicIpsRequest.


        :return: The limit of this ListPublicIpsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPublicIpsRequest.


        :param limit: The limit of this ListPublicIpsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListPublicIpsRequest.


        :return: The offset of this ListPublicIpsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPublicIpsRequest.


        :param offset: The offset of this ListPublicIpsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def site_id(self):
        """Gets the site_id of this ListPublicIpsRequest.


        :return: The site_id of this ListPublicIpsRequest.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this ListPublicIpsRequest.


        :param site_id: The site_id of this ListPublicIpsRequest.
        :type: str
        """
        self._site_id = site_id

    @property
    def port_id(self):
        """Gets the port_id of this ListPublicIpsRequest.


        :return: The port_id of this ListPublicIpsRequest.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this ListPublicIpsRequest.


        :param port_id: The port_id of this ListPublicIpsRequest.
        :type: str
        """
        self._port_id = port_id

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
                if attr in self.sensitive_list:
                    result[attr] = "****"
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
        if not isinstance(other, ListPublicIpsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other