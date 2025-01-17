# coding: utf-8

import pprint
import re

import six





class QuerySample:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'dimensions': 'list[Dimension]',
        'metric_name': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'dimensions': 'dimensions',
        'metric_name': 'metric_name'
    }

    def __init__(self, namespace=None, dimensions=None, metric_name=None):
        """QuerySample - a model defined in huaweicloud sdk"""
        
        

        self._namespace = None
        self._dimensions = None
        self._metric_name = None
        self.discriminator = None

        self.namespace = namespace
        self.dimensions = dimensions
        self.metric_name = metric_name

    @property
    def namespace(self):
        """Gets the namespace of this QuerySample.

        时间序列的命名空间。 取值范围  PAAS.CONTAINER PAAS.NODE PAAS.SLA PAAS.AGGR CUSTOMMETRICS 

        :return: The namespace of this QuerySample.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this QuerySample.

        时间序列的命名空间。 取值范围  PAAS.CONTAINER PAAS.NODE PAAS.SLA PAAS.AGGR CUSTOMMETRICS 

        :param namespace: The namespace of this QuerySample.
        :type: str
        """
        self._namespace = namespace

    @property
    def dimensions(self):
        """Gets the dimensions of this QuerySample.

        时间序列维度列表。 取值范围： 数组不能为空，同时数组中任何一个dimension对象name和value属性的值也不能为空。 

        :return: The dimensions of this QuerySample.
        :rtype: list[Dimension]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this QuerySample.

        时间序列维度列表。 取值范围： 数组不能为空，同时数组中任何一个dimension对象name和value属性的值也不能为空。 

        :param dimensions: The dimensions of this QuerySample.
        :type: list[Dimension]
        """
        self._dimensions = dimensions

    @property
    def metric_name(self):
        """Gets the metric_name of this QuerySample.

        时间序列名称。 取值范围 名称长度为1~255个字符 

        :return: The metric_name of this QuerySample.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this QuerySample.

        时间序列名称。 取值范围 名称长度为1~255个字符 

        :param metric_name: The metric_name of this QuerySample.
        :type: str
        """
        self._metric_name = metric_name

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
        if not isinstance(other, QuerySample):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
