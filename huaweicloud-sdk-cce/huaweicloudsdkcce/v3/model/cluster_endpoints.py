# coding: utf-8

import pprint
import re

import six





class ClusterEndpoints:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'type': 'str'
    }

    attribute_map = {
        'url': 'url',
        'type': 'type'
    }

    def __init__(self, url=None, type=None):
        """ClusterEndpoints - a model defined in huaweicloud sdk"""
        
        

        self._url = None
        self._type = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if type is not None:
            self.type = type

    @property
    def url(self):
        """Gets the url of this ClusterEndpoints.

        集群中 kube-apiserver 的访问地址

        :return: The url of this ClusterEndpoints.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ClusterEndpoints.

        集群中 kube-apiserver 的访问地址

        :param url: The url of this ClusterEndpoints.
        :type: str
        """
        self._url = url

    @property
    def type(self):
        """Gets the type of this ClusterEndpoints.

        集群访问地址的类型 - Internal：用户子网内访问的地址 - External：公网访问的地址

        :return: The type of this ClusterEndpoints.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ClusterEndpoints.

        集群访问地址的类型 - Internal：用户子网内访问的地址 - External：公网访问的地址

        :param type: The type of this ClusterEndpoints.
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
        if not isinstance(other, ClusterEndpoints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
