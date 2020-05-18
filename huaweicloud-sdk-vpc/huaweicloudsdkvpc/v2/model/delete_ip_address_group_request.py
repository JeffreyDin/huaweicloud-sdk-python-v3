# coding: utf-8

import pprint
import re

import six


class DeleteIpAddressGroupRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'address_group_id': 'str'
    }

    attribute_map = {
        'address_group_id': 'address_group_id'
    }

    def __init__(self, address_group_id=None):  # noqa: E501
        """DeleteIpAddressGroupRequest - a model defined in huaweicloud sdk"""

        self._address_group_id = None
        self.discriminator = None

        self.address_group_id = address_group_id

    @property
    def address_group_id(self):
        """Gets the address_group_id of this DeleteIpAddressGroupRequest.


        :return: The address_group_id of this DeleteIpAddressGroupRequest.
        :rtype: str
        """
        return self._address_group_id

    @address_group_id.setter
    def address_group_id(self, address_group_id):
        """Sets the address_group_id of this DeleteIpAddressGroupRequest.


        :param address_group_id: The address_group_id of this DeleteIpAddressGroupRequest.
        :type: str
        """
        self._address_group_id = address_group_id

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
        if not isinstance(other, DeleteIpAddressGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other