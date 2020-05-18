# coding: utf-8

import pprint
import re

import six


class RegisterFpgaImageResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'fpga_image': 'RegisterFpgaImageResult'
    }

    attribute_map = {
        'fpga_image': 'fpga_image'
    }

    def __init__(self, fpga_image=None):  # noqa: E501
        """RegisterFpgaImageResponse - a model defined in huaweicloud sdk"""

        self._fpga_image = None
        self.discriminator = None

        if fpga_image is not None:
            self.fpga_image = fpga_image

    @property
    def fpga_image(self):
        """Gets the fpga_image of this RegisterFpgaImageResponse.


        :return: The fpga_image of this RegisterFpgaImageResponse.
        :rtype: RegisterFpgaImageResult
        """
        return self._fpga_image

    @fpga_image.setter
    def fpga_image(self, fpga_image):
        """Sets the fpga_image of this RegisterFpgaImageResponse.


        :param fpga_image: The fpga_image of this RegisterFpgaImageResponse.
        :type: RegisterFpgaImageResult
        """
        self._fpga_image = fpga_image

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
        if not isinstance(other, RegisterFpgaImageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other