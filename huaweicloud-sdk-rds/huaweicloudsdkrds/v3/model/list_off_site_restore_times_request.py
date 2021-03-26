# coding: utf-8

import pprint
import re

import six





class ListOffSiteRestoreTimesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'date': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'date': 'date'
    }

    def __init__(self, x_language=None, instance_id=None, date=None):
        """ListOffSiteRestoreTimesRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_language = None
        self._instance_id = None
        self._date = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        if date is not None:
            self.date = date

    @property
    def x_language(self):
        """Gets the x_language of this ListOffSiteRestoreTimesRequest.


        :return: The x_language of this ListOffSiteRestoreTimesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListOffSiteRestoreTimesRequest.


        :param x_language: The x_language of this ListOffSiteRestoreTimesRequest.
        :type: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        """Gets the instance_id of this ListOffSiteRestoreTimesRequest.


        :return: The instance_id of this ListOffSiteRestoreTimesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListOffSiteRestoreTimesRequest.


        :param instance_id: The instance_id of this ListOffSiteRestoreTimesRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def date(self):
        """Gets the date of this ListOffSiteRestoreTimesRequest.


        :return: The date of this ListOffSiteRestoreTimesRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this ListOffSiteRestoreTimesRequest.


        :param date: The date of this ListOffSiteRestoreTimesRequest.
        :type: str
        """
        self._date = date

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
        if not isinstance(other, ListOffSiteRestoreTimesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other