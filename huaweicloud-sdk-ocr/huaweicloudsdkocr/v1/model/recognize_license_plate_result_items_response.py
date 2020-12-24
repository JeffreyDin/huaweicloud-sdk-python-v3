# coding: utf-8

import pprint
import re

import six





class RecognizeLicensePlateResultItemsResponse:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'plate_number': 'str',
        'plate_color': 'str',
        'confidence': 'float',
        'plate_location': 'list[int]'
    }

    attribute_map = {
        'plate_number': 'plate_number',
        'plate_color': 'plate_color',
        'confidence': 'confidence',
        'plate_location': 'plate_location'
    }

    def __init__(self, plate_number=None, plate_color=None, confidence=None, plate_location=None):
        """RecognizeLicensePlateResultItemsResponse - a model defined in huaweicloud sdk"""
        
        

        self._plate_number = None
        self._plate_color = None
        self._confidence = None
        self._plate_location = None
        self.discriminator = None

        self.plate_number = plate_number
        self.plate_color = plate_color
        self.confidence = confidence
        self.plate_location = plate_location

    @property
    def plate_number(self):
        """Gets the plate_number of this RecognizeLicensePlateResultItemsResponse.

        车牌内容。 

        :return: The plate_number of this RecognizeLicensePlateResultItemsResponse.
        :rtype: str
        """
        return self._plate_number

    @plate_number.setter
    def plate_number(self, plate_number):
        """Sets the plate_number of this RecognizeLicensePlateResultItemsResponse.

        车牌内容。 

        :param plate_number: The plate_number of this RecognizeLicensePlateResultItemsResponse.
        :type: str
        """
        self._plate_number = plate_number

    @property
    def plate_color(self):
        """Gets the plate_color of this RecognizeLicensePlateResultItemsResponse.

        识别出的车牌底色。 

        :return: The plate_color of this RecognizeLicensePlateResultItemsResponse.
        :rtype: str
        """
        return self._plate_color

    @plate_color.setter
    def plate_color(self, plate_color):
        """Sets the plate_color of this RecognizeLicensePlateResultItemsResponse.

        识别出的车牌底色。 

        :param plate_color: The plate_color of this RecognizeLicensePlateResultItemsResponse.
        :type: str
        """
        self._plate_color = plate_color

    @property
    def confidence(self):
        """Gets the confidence of this RecognizeLicensePlateResultItemsResponse.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 

        :return: The confidence of this RecognizeLicensePlateResultItemsResponse.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this RecognizeLicensePlateResultItemsResponse.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 

        :param confidence: The confidence of this RecognizeLicensePlateResultItemsResponse.
        :type: float
        """
        self._confidence = confidence

    @property
    def plate_location(self):
        """Gets the plate_location of this RecognizeLicensePlateResultItemsResponse.

        车牌的区域位置信息，列表形式，包含文字区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The plate_location of this RecognizeLicensePlateResultItemsResponse.
        :rtype: list[int]
        """
        return self._plate_location

    @plate_location.setter
    def plate_location(self, plate_location):
        """Sets the plate_location of this RecognizeLicensePlateResultItemsResponse.

        车牌的区域位置信息，列表形式，包含文字区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param plate_location: The plate_location of this RecognizeLicensePlateResultItemsResponse.
        :type: list[int]
        """
        self._plate_location = plate_location

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
        if not isinstance(other, RecognizeLicensePlateResultItemsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
