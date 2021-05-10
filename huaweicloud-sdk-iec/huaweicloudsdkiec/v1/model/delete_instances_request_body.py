# coding: utf-8

import pprint
import re

import six





class DeleteInstancesRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'servers': 'list[BaseId]'
    }

    attribute_map = {
        'servers': 'servers'
    }

    def __init__(self, servers=None):
        """DeleteInstancesRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._servers = None
        self.discriminator = None

        self.servers = servers

    @property
    def servers(self):
        """Gets the servers of this DeleteInstancesRequestBody.

        边缘实例ID列表。 > IEC默认同步删除边缘实例的弹性公网IP和磁盘。

        :return: The servers of this DeleteInstancesRequestBody.
        :rtype: list[BaseId]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this DeleteInstancesRequestBody.

        边缘实例ID列表。 > IEC默认同步删除边缘实例的弹性公网IP和磁盘。

        :param servers: The servers of this DeleteInstancesRequestBody.
        :type: list[BaseId]
        """
        self._servers = servers

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
        if not isinstance(other, DeleteInstancesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
