# coding: utf-8

import pprint
import re

import six


class MigrateServerOption(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'dedicated_host_id': 'str'
    }

    attribute_map = {
        'dedicated_host_id': 'dedicated_host_id'
    }

    def __init__(self, dedicated_host_id=None):  # noqa: E501
        """MigrateServerOption - a model defined in huaweicloud sdk"""

        self._dedicated_host_id = None
        self.discriminator = None

        if dedicated_host_id is not None:
            self.dedicated_host_id = dedicated_host_id

    @property
    def dedicated_host_id(self):
        """Gets the dedicated_host_id of this MigrateServerOption.

        专属主机ID。  当弹性云服务器从公共资源池迁移至专属主机上，或者弹性云服务器在专属主机之间迁移时，该字段生效。

        :return: The dedicated_host_id of this MigrateServerOption.
        :rtype: str
        """
        return self._dedicated_host_id

    @dedicated_host_id.setter
    def dedicated_host_id(self, dedicated_host_id):
        """Sets the dedicated_host_id of this MigrateServerOption.

        专属主机ID。  当弹性云服务器从公共资源池迁移至专属主机上，或者弹性云服务器在专属主机之间迁移时，该字段生效。

        :param dedicated_host_id: The dedicated_host_id of this MigrateServerOption.
        :type: str
        """
        self._dedicated_host_id = dedicated_host_id

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
        if not isinstance(other, MigrateServerOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other