# coding: utf-8

import pprint
import re

import six





class ListFlavorsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'name': 'str',
        'area': 'str',
        'province': 'str',
        'city': 'str',
        'operator': 'str',
        'id': 'str',
        'site_ids': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'area': 'area',
        'province': 'province',
        'city': 'city',
        'operator': 'operator',
        'id': 'id',
        'site_ids': 'site_ids'
    }

    def __init__(self, offset=None, limit=None, name=None, area=None, province=None, city=None, operator=None, id=None, site_ids=None):
        """ListFlavorsRequest - a model defined in huaweicloud sdk"""
        
        

        self._offset = None
        self._limit = None
        self._name = None
        self._area = None
        self._province = None
        self._city = None
        self._operator = None
        self._id = None
        self._site_ids = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if area is not None:
            self.area = area
        if province is not None:
            self.province = province
        if city is not None:
            self.city = city
        if operator is not None:
            self.operator = operator
        if id is not None:
            self.id = id
        if site_ids is not None:
            self.site_ids = site_ids

    @property
    def offset(self):
        """Gets the offset of this ListFlavorsRequest.


        :return: The offset of this ListFlavorsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListFlavorsRequest.


        :param offset: The offset of this ListFlavorsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListFlavorsRequest.


        :return: The limit of this ListFlavorsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListFlavorsRequest.


        :param limit: The limit of this ListFlavorsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ListFlavorsRequest.


        :return: The name of this ListFlavorsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListFlavorsRequest.


        :param name: The name of this ListFlavorsRequest.
        :type: str
        """
        self._name = name

    @property
    def area(self):
        """Gets the area of this ListFlavorsRequest.


        :return: The area of this ListFlavorsRequest.
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this ListFlavorsRequest.


        :param area: The area of this ListFlavorsRequest.
        :type: str
        """
        self._area = area

    @property
    def province(self):
        """Gets the province of this ListFlavorsRequest.


        :return: The province of this ListFlavorsRequest.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """Sets the province of this ListFlavorsRequest.


        :param province: The province of this ListFlavorsRequest.
        :type: str
        """
        self._province = province

    @property
    def city(self):
        """Gets the city of this ListFlavorsRequest.


        :return: The city of this ListFlavorsRequest.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ListFlavorsRequest.


        :param city: The city of this ListFlavorsRequest.
        :type: str
        """
        self._city = city

    @property
    def operator(self):
        """Gets the operator of this ListFlavorsRequest.


        :return: The operator of this ListFlavorsRequest.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this ListFlavorsRequest.


        :param operator: The operator of this ListFlavorsRequest.
        :type: str
        """
        self._operator = operator

    @property
    def id(self):
        """Gets the id of this ListFlavorsRequest.


        :return: The id of this ListFlavorsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListFlavorsRequest.


        :param id: The id of this ListFlavorsRequest.
        :type: str
        """
        self._id = id

    @property
    def site_ids(self):
        """Gets the site_ids of this ListFlavorsRequest.


        :return: The site_ids of this ListFlavorsRequest.
        :rtype: str
        """
        return self._site_ids

    @site_ids.setter
    def site_ids(self, site_ids):
        """Sets the site_ids of this ListFlavorsRequest.


        :param site_ids: The site_ids of this ListFlavorsRequest.
        :type: str
        """
        self._site_ids = site_ids

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
        if not isinstance(other, ListFlavorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other