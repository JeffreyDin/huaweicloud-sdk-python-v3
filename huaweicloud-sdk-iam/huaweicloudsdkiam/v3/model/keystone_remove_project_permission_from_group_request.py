# coding: utf-8

import pprint
import re

import six


class KeystoneRemoveProjectPermissionFromGroupRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'project_id': 'str',
        'group_id': 'str',
        'role_id': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'group_id': 'group_id',
        'role_id': 'role_id'
    }

    def __init__(self, project_id=None, group_id=None, role_id=None):  # noqa: E501
        """KeystoneRemoveProjectPermissionFromGroupRequest - a model defined in huaweicloud sdk"""

        self._project_id = None
        self._group_id = None
        self._role_id = None
        self.discriminator = None

        self.project_id = project_id
        self.group_id = group_id
        self.role_id = role_id

    @property
    def project_id(self):
        """Gets the project_id of this KeystoneRemoveProjectPermissionFromGroupRequest.


        :return: The project_id of this KeystoneRemoveProjectPermissionFromGroupRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this KeystoneRemoveProjectPermissionFromGroupRequest.


        :param project_id: The project_id of this KeystoneRemoveProjectPermissionFromGroupRequest.
        :type: str
        """
        self._project_id = project_id

    @property
    def group_id(self):
        """Gets the group_id of this KeystoneRemoveProjectPermissionFromGroupRequest.


        :return: The group_id of this KeystoneRemoveProjectPermissionFromGroupRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this KeystoneRemoveProjectPermissionFromGroupRequest.


        :param group_id: The group_id of this KeystoneRemoveProjectPermissionFromGroupRequest.
        :type: str
        """
        self._group_id = group_id

    @property
    def role_id(self):
        """Gets the role_id of this KeystoneRemoveProjectPermissionFromGroupRequest.


        :return: The role_id of this KeystoneRemoveProjectPermissionFromGroupRequest.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this KeystoneRemoveProjectPermissionFromGroupRequest.


        :param role_id: The role_id of this KeystoneRemoveProjectPermissionFromGroupRequest.
        :type: str
        """
        self._role_id = role_id

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
        if not isinstance(other, KeystoneRemoveProjectPermissionFromGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other