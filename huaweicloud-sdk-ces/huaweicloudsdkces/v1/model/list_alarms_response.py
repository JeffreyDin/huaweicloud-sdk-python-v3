# coding: utf-8

import pprint
import re

import six


class ListAlarmsResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'metric_alarms': 'list[MetricAlarms]',
        'meta_data': 'MetaData'
    }

    attribute_map = {
        'metric_alarms': 'metric_alarms',
        'meta_data': 'meta_data'
    }

    def __init__(self, metric_alarms=None, meta_data=None):  # noqa: E501
        """ListAlarmsResponse - a model defined in huaweicloud sdk"""

        self._metric_alarms = None
        self._meta_data = None
        self.discriminator = None

        if metric_alarms is not None:
            self.metric_alarms = metric_alarms
        if meta_data is not None:
            self.meta_data = meta_data

    @property
    def metric_alarms(self):
        """Gets the metric_alarms of this ListAlarmsResponse.

        

        :return: The metric_alarms of this ListAlarmsResponse.
        :rtype: list[MetricAlarms]
        """
        return self._metric_alarms

    @metric_alarms.setter
    def metric_alarms(self, metric_alarms):
        """Sets the metric_alarms of this ListAlarmsResponse.

        

        :param metric_alarms: The metric_alarms of this ListAlarmsResponse.
        :type: list[MetricAlarms]
        """
        self._metric_alarms = metric_alarms

    @property
    def meta_data(self):
        """Gets the meta_data of this ListAlarmsResponse.


        :return: The meta_data of this ListAlarmsResponse.
        :rtype: MetaData
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this ListAlarmsResponse.


        :param meta_data: The meta_data of this ListAlarmsResponse.
        :type: MetaData
        """
        self._meta_data = meta_data

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
        if not isinstance(other, ListAlarmsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other