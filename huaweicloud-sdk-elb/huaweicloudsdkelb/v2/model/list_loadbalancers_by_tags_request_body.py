# coding: utf-8

import pprint
import re

import six





class ListLoadbalancersByTagsRequestBody:


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
        'action': 'str',
        'matches': 'list[ActionMatch]',
        'tags': 'list[ActionTag]',
        'without_any_tag': 'bool'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'action': 'action',
        'matches': 'matches',
        'tags': 'tags',
        'without_any_tag': 'without_any_tag'
    }

    def __init__(self, offset=None, limit=None, action=None, matches=None, tags=None, without_any_tag=None):
        """ListLoadbalancersByTagsRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._offset = None
        self._limit = None
        self._action = None
        self._matches = None
        self._tags = None
        self._without_any_tag = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.action = action
        if matches is not None:
            self.matches = matches
        if tags is not None:
            self.tags = tags
        if without_any_tag is not None:
            self.without_any_tag = without_any_tag

    @property
    def offset(self):
        """Gets the offset of this ListLoadbalancersByTagsRequestBody.

        分页起始。

        :return: The offset of this ListLoadbalancersByTagsRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListLoadbalancersByTagsRequestBody.

        分页起始。

        :param offset: The offset of this ListLoadbalancersByTagsRequestBody.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListLoadbalancersByTagsRequestBody.

        分页大小。

        :return: The limit of this ListLoadbalancersByTagsRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListLoadbalancersByTagsRequestBody.

        分页大小。

        :param limit: The limit of this ListLoadbalancersByTagsRequestBody.
        :type: int
        """
        self._limit = limit

    @property
    def action(self):
        """Gets the action of this ListLoadbalancersByTagsRequestBody.

        操作标识（仅限于filter，count）： filter（过滤），如果是filter就是分页查询 count(查询总条数)，按照条件将总条数返回。

        :return: The action of this ListLoadbalancersByTagsRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ListLoadbalancersByTagsRequestBody.

        操作标识（仅限于filter，count）： filter（过滤），如果是filter就是分页查询 count(查询总条数)，按照条件将总条数返回。

        :param action: The action of this ListLoadbalancersByTagsRequestBody.
        :type: str
        """
        self._action = action

    @property
    def matches(self):
        """Gets the matches of this ListLoadbalancersByTagsRequestBody.

        搜索字段，key为要匹配的字段，如resource_name等。value为匹配的值。key为固定字典值。根据不同的字段确认是否需要模糊匹配，如resource_name默认为模糊搜索，如果value为空字符串精确匹配。key如果是resource_id则精确匹配。

        :return: The matches of this ListLoadbalancersByTagsRequestBody.
        :rtype: list[ActionMatch]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this ListLoadbalancersByTagsRequestBody.

        搜索字段，key为要匹配的字段，如resource_name等。value为匹配的值。key为固定字典值。根据不同的字段确认是否需要模糊匹配，如resource_name默认为模糊搜索，如果value为空字符串精确匹配。key如果是resource_id则精确匹配。

        :param matches: The matches of this ListLoadbalancersByTagsRequestBody.
        :type: list[ActionMatch]
        """
        self._matches = matches

    @property
    def tags(self):
        """Gets the tags of this ListLoadbalancersByTagsRequestBody.

        要搜索的标签值

        :return: The tags of this ListLoadbalancersByTagsRequestBody.
        :rtype: list[ActionTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListLoadbalancersByTagsRequestBody.

        要搜索的标签值

        :param tags: The tags of this ListLoadbalancersByTagsRequestBody.
        :type: list[ActionTag]
        """
        self._tags = tags

    @property
    def without_any_tag(self):
        """Gets the without_any_tag of this ListLoadbalancersByTagsRequestBody.

        查询不包含任何标签的资源，该字段为true时，忽略tags字段的查询条件。

        :return: The without_any_tag of this ListLoadbalancersByTagsRequestBody.
        :rtype: bool
        """
        return self._without_any_tag

    @without_any_tag.setter
    def without_any_tag(self, without_any_tag):
        """Sets the without_any_tag of this ListLoadbalancersByTagsRequestBody.

        查询不包含任何标签的资源，该字段为true时，忽略tags字段的查询条件。

        :param without_any_tag: The without_any_tag of this ListLoadbalancersByTagsRequestBody.
        :type: bool
        """
        self._without_any_tag = without_any_tag

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
        if not isinstance(other, ListLoadbalancersByTagsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other