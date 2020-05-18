# coding: utf-8

import pprint
import re

import six


class GlanceUpdateImageRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'image_id': 'str',
        'body': 'list[GlanceUpdateImageRequestBody]'
    }

    attribute_map = {
        'image_id': 'image_id',
        'body': 'body'
    }

    def __init__(self, image_id=None, body=None):  # noqa: E501
        """GlanceUpdateImageRequest - a model defined in huaweicloud sdk"""

        self._image_id = None
        self._body = None
        self.discriminator = None

        self.image_id = image_id
        if body is not None:
            self.body = body

    @property
    def image_id(self):
        """Gets the image_id of this GlanceUpdateImageRequest.


        :return: The image_id of this GlanceUpdateImageRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this GlanceUpdateImageRequest.


        :param image_id: The image_id of this GlanceUpdateImageRequest.
        :type: str
        """
        self._image_id = image_id

    @property
    def body(self):
        """Gets the body of this GlanceUpdateImageRequest.


        :return: The body of this GlanceUpdateImageRequest.
        :rtype: list[GlanceUpdateImageRequestBody]
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this GlanceUpdateImageRequest.


        :param body: The body of this GlanceUpdateImageRequest.
        :type: list[GlanceUpdateImageRequestBody]
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
        if not isinstance(other, GlanceUpdateImageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other