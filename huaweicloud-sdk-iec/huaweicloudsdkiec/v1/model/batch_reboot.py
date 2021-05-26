# coding: utf-8

import pprint
import re

import six





class BatchReboot:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'servers': 'list[BaseId]',
        'type': 'str'
    }

    attribute_map = {
        'servers': 'servers',
        'type': 'type'
    }

    def __init__(self, servers=None, type=None):
        """BatchReboot - a model defined in huaweicloud sdk"""
        
        

        self._servers = None
        self._type = None
        self.discriminator = None

        if servers is not None:
            self.servers = servers
        if type is not None:
            self.type = type

    @property
    def servers(self):
        """Gets the servers of this BatchReboot.

        待重启的边缘实例列表。

        :return: The servers of this BatchReboot.
        :rtype: list[BaseId]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this BatchReboot.

        待重启的边缘实例列表。

        :param servers: The servers of this BatchReboot.
        :type: list[BaseId]
        """
        self._servers = servers

    @property
    def type(self):
        """Gets the type of this BatchReboot.

        重启类型：   - SOFT：普通重启。  - HARD：强制重启。  > 重启必须指定重启类型。

        :return: The type of this BatchReboot.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BatchReboot.

        重启类型：   - SOFT：普通重启。  - HARD：强制重启。  > 重启必须指定重启类型。

        :param type: The type of this BatchReboot.
        :type: str
        """
        self._type = type

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
        if not isinstance(other, BatchReboot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other