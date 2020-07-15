# coding: utf-8

import pprint
import re

import six





class UpdateUserInformationRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'user_id': 'str',
        'body': 'UpdateUserInformationRequestBody'
    }

    attribute_map = {
        'user_id': 'user_id',
        'body': 'body'
    }

    def __init__(self, user_id=None, body=None):
        """UpdateUserInformationRequest - a model defined in huaweicloud sdk"""
        
        

        self._user_id = None
        self._body = None
        self.discriminator = None

        self.user_id = user_id
        if body is not None:
            self.body = body

    @property
    def user_id(self):
        """Gets the user_id of this UpdateUserInformationRequest.


        :return: The user_id of this UpdateUserInformationRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UpdateUserInformationRequest.


        :param user_id: The user_id of this UpdateUserInformationRequest.
        :type: str
        """
        self._user_id = user_id

    @property
    def body(self):
        """Gets the body of this UpdateUserInformationRequest.


        :return: The body of this UpdateUserInformationRequest.
        :rtype: UpdateUserInformationRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateUserInformationRequest.


        :param body: The body of this UpdateUserInformationRequest.
        :type: UpdateUserInformationRequestBody
        """
        self._body = body

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
        if not isinstance(other, UpdateUserInformationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other