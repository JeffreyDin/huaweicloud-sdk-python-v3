# coding: utf-8

import pprint
import re

import six





class RootVolume:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'volume_type': 'str'
    }

    attribute_map = {
        'size': 'size',
        'volume_type': 'volume_type'
    }

    def __init__(self, size=None, volume_type=None):
        """RootVolume - a model defined in huaweicloud sdk"""
        
        

        self._size = None
        self._volume_type = None
        self.discriminator = None

        self.size = size
        self.volume_type = volume_type

    @property
    def size(self):
        """Gets the size of this RootVolume.

        系统盘大小，容量单位为GB，输入大小范围为[40,100]。

        :return: The size of this RootVolume.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this RootVolume.

        系统盘大小，容量单位为GB，输入大小范围为[40,100]。

        :param size: The size of this RootVolume.
        :type: int
        """
        self._size = size

    @property
    def volume_type(self):
        """Gets the volume_type of this RootVolume.

        边缘实例系统盘对应的磁盘类型，需要与站点所提供的磁盘类型相匹配。

        :return: The volume_type of this RootVolume.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this RootVolume.

        边缘实例系统盘对应的磁盘类型，需要与站点所提供的磁盘类型相匹配。

        :param volume_type: The volume_type of this RootVolume.
        :type: str
        """
        self._volume_type = volume_type

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
        if not isinstance(other, RootVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
