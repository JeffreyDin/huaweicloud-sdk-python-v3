# coding: utf-8

import pprint
import re

import six





class SubDetail:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'substep_name': 'str',
        'detail': 'str',
        'status': 'str',
        'message': 'list[str]',
        'start_time': 'int',
        'end_time': 'int',
        'serial_num': 'int'
    }

    attribute_map = {
        'substep_name': 'substep_name',
        'detail': 'detail',
        'status': 'status',
        'message': 'message',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'serial_num': 'serial_num'
    }

    def __init__(self, substep_name=None, detail=None, status=None, message=None, start_time=None, end_time=None, serial_num=None):
        """SubDetail - a model defined in huaweicloud sdk"""
        
        

        self._substep_name = None
        self._detail = None
        self._status = None
        self._message = None
        self._start_time = None
        self._end_time = None
        self._serial_num = None
        self.discriminator = None

        if substep_name is not None:
            self.substep_name = substep_name
        if detail is not None:
            self.detail = detail
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if serial_num is not None:
            self.serial_num = serial_num

    @property
    def substep_name(self):
        """Gets the substep_name of this SubDetail.

        子操作名

        :return: The substep_name of this SubDetail.
        :rtype: str
        """
        return self._substep_name

    @substep_name.setter
    def substep_name(self, substep_name):
        """Sets the substep_name of this SubDetail.

        子操作名

        :param substep_name: The substep_name of this SubDetail.
        :type: str
        """
        self._substep_name = substep_name

    @property
    def detail(self):
        """Gets the detail of this SubDetail.

        子操作详情

        :return: The detail of this SubDetail.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this SubDetail.

        子操作详情

        :param detail: The detail of this SubDetail.
        :type: str
        """
        self._detail = detail

    @property
    def status(self):
        """Gets the status of this SubDetail.

        子操作状态

        :return: The status of this SubDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SubDetail.

        子操作状态

        :param status: The status of this SubDetail.
        :type: str
        """
        self._status = status

    @property
    def message(self):
        """Gets the message of this SubDetail.

        子操作过程信息记录

        :return: The message of this SubDetail.
        :rtype: list[str]
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this SubDetail.

        子操作过程信息记录

        :param message: The message of this SubDetail.
        :type: list[str]
        """
        self._message = message

    @property
    def start_time(self):
        """Gets the start_time of this SubDetail.

        开始时间

        :return: The start_time of this SubDetail.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this SubDetail.

        开始时间

        :param start_time: The start_time of this SubDetail.
        :type: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this SubDetail.

        结束时间

        :return: The end_time of this SubDetail.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this SubDetail.

        结束时间

        :param end_time: The end_time of this SubDetail.
        :type: int
        """
        self._end_time = end_time

    @property
    def serial_num(self):
        """Gets the serial_num of this SubDetail.

        序列号

        :return: The serial_num of this SubDetail.
        :rtype: int
        """
        return self._serial_num

    @serial_num.setter
    def serial_num(self, serial_num):
        """Sets the serial_num of this SubDetail.

        序列号

        :param serial_num: The serial_num of this SubDetail.
        :type: int
        """
        self._serial_num = serial_num

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
        if not isinstance(other, SubDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other