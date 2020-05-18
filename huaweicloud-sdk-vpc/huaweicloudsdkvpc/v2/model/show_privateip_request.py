# coding: utf-8

import pprint
import re

import six


class ShowPrivateipRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'privateip_id': 'str'
    }

    attribute_map = {
        'privateip_id': 'privateip_id'
    }

    def __init__(self, privateip_id=None):  # noqa: E501
        """ShowPrivateipRequest - a model defined in huaweicloud sdk"""

        self._privateip_id = None
        self.discriminator = None

        self.privateip_id = privateip_id

    @property
    def privateip_id(self):
        """Gets the privateip_id of this ShowPrivateipRequest.


        :return: The privateip_id of this ShowPrivateipRequest.
        :rtype: str
        """
        return self._privateip_id

    @privateip_id.setter
    def privateip_id(self, privateip_id):
        """Sets the privateip_id of this ShowPrivateipRequest.


        :param privateip_id: The privateip_id of this ShowPrivateipRequest.
        :type: str
        """
        self._privateip_id = privateip_id

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
        if not isinstance(other, ShowPrivateipRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other