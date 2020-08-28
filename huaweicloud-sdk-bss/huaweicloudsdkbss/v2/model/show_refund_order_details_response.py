# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowRefundOrderDetailsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'refund_infos': 'list[OrderRefundInfoV2]',
        'total_count': 'int'
    }

    attribute_map = {
        'refund_infos': 'refund_infos',
        'total_count': 'total_count'
    }

    def __init__(self, refund_infos=None, total_count=None):
        """ShowRefundOrderDetailsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._refund_infos = None
        self._total_count = None
        self.discriminator = None

        if refund_infos is not None:
            self.refund_infos = refund_infos
        if total_count is not None:
            self.total_count = total_count

    @property
    def refund_infos(self):
        """Gets the refund_infos of this ShowRefundOrderDetailsResponse.

        |参数名称：资源信息列表。具体请参见表2 OrderRefundInfoV2。| |参数约束以及描述：资源信息列表。具体请参见表2 OrderRefundInfoV2。|

        :return: The refund_infos of this ShowRefundOrderDetailsResponse.
        :rtype: list[OrderRefundInfoV2]
        """
        return self._refund_infos

    @refund_infos.setter
    def refund_infos(self, refund_infos):
        """Sets the refund_infos of this ShowRefundOrderDetailsResponse.

        |参数名称：资源信息列表。具体请参见表2 OrderRefundInfoV2。| |参数约束以及描述：资源信息列表。具体请参见表2 OrderRefundInfoV2。|

        :param refund_infos: The refund_infos of this ShowRefundOrderDetailsResponse.
        :type: list[OrderRefundInfoV2]
        """
        self._refund_infos = refund_infos

    @property
    def total_count(self):
        """Gets the total_count of this ShowRefundOrderDetailsResponse.

        |参数名称：总记录数。| |参数的约束及描述：总记录数。|

        :return: The total_count of this ShowRefundOrderDetailsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ShowRefundOrderDetailsResponse.

        |参数名称：总记录数。| |参数的约束及描述：总记录数。|

        :param total_count: The total_count of this ShowRefundOrderDetailsResponse.
        :type: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ShowRefundOrderDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other