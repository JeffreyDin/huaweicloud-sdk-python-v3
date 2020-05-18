# coding: utf-8

import pprint
import re

import six


class NovaKeypairDetail(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'public_key': 'str',
        'name': 'str',
        'fingerprint': 'str',
        'created_at': 'datetime',
        'deleted': 'bool',
        'deleted_at': 'datetime',
        'id': 'str',
        'updated_at': 'datetime',
        'user_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'public_key': 'public_key',
        'name': 'name',
        'fingerprint': 'fingerprint',
        'created_at': 'created_at',
        'deleted': 'deleted',
        'deleted_at': 'deleted_at',
        'id': 'id',
        'updated_at': 'updated_at',
        'user_id': 'user_id',
        'type': 'type'
    }

    def __init__(self, public_key=None, name=None, fingerprint=None, created_at=None, deleted=None, deleted_at=None, id=None, updated_at=None, user_id=None, type=None):  # noqa: E501
        """NovaKeypairDetail - a model defined in huaweicloud sdk"""

        self._public_key = None
        self._name = None
        self._fingerprint = None
        self._created_at = None
        self._deleted = None
        self._deleted_at = None
        self._id = None
        self._updated_at = None
        self._user_id = None
        self._type = None
        self.discriminator = None

        self.public_key = public_key
        self.name = name
        self.fingerprint = fingerprint
        self.created_at = created_at
        self.deleted = deleted
        self.deleted_at = deleted_at
        self.id = id
        self.updated_at = updated_at
        self.user_id = user_id
        if type is not None:
            self.type = type

    @property
    def public_key(self):
        """Gets the public_key of this NovaKeypairDetail.

        密钥对应publicKey信息。

        :return: The public_key of this NovaKeypairDetail.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this NovaKeypairDetail.

        密钥对应publicKey信息。

        :param public_key: The public_key of this NovaKeypairDetail.
        :type: str
        """
        self._public_key = public_key

    @property
    def name(self):
        """Gets the name of this NovaKeypairDetail.

        密钥名称。

        :return: The name of this NovaKeypairDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NovaKeypairDetail.

        密钥名称。

        :param name: The name of this NovaKeypairDetail.
        :type: str
        """
        self._name = name

    @property
    def fingerprint(self):
        """Gets the fingerprint of this NovaKeypairDetail.

        密钥对应指纹信息。

        :return: The fingerprint of this NovaKeypairDetail.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this NovaKeypairDetail.

        密钥对应指纹信息。

        :param fingerprint: The fingerprint of this NovaKeypairDetail.
        :type: str
        """
        self._fingerprint = fingerprint

    @property
    def created_at(self):
        """Gets the created_at of this NovaKeypairDetail.

        密钥创建时间。

        :return: The created_at of this NovaKeypairDetail.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this NovaKeypairDetail.

        密钥创建时间。

        :param created_at: The created_at of this NovaKeypairDetail.
        :type: datetime
        """
        self._created_at = created_at

    @property
    def deleted(self):
        """Gets the deleted of this NovaKeypairDetail.

        密钥删除标记。   - true，表示密钥已被删除。   - false，表示密钥未被删除。

        :return: The deleted of this NovaKeypairDetail.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this NovaKeypairDetail.

        密钥删除标记。   - true，表示密钥已被删除。   - false，表示密钥未被删除。

        :param deleted: The deleted of this NovaKeypairDetail.
        :type: bool
        """
        self._deleted = deleted

    @property
    def deleted_at(self):
        """Gets the deleted_at of this NovaKeypairDetail.

        密钥删除时间。

        :return: The deleted_at of this NovaKeypairDetail.
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this NovaKeypairDetail.

        密钥删除时间。

        :param deleted_at: The deleted_at of this NovaKeypairDetail.
        :type: datetime
        """
        self._deleted_at = deleted_at

    @property
    def id(self):
        """Gets the id of this NovaKeypairDetail.

        密钥ID。

        :return: The id of this NovaKeypairDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NovaKeypairDetail.

        密钥ID。

        :param id: The id of this NovaKeypairDetail.
        :type: str
        """
        self._id = id

    @property
    def updated_at(self):
        """Gets the updated_at of this NovaKeypairDetail.

        密钥更新时间。

        :return: The updated_at of this NovaKeypairDetail.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this NovaKeypairDetail.

        密钥更新时间。

        :param updated_at: The updated_at of this NovaKeypairDetail.
        :type: datetime
        """
        self._updated_at = updated_at

    @property
    def user_id(self):
        """Gets the user_id of this NovaKeypairDetail.

        密钥所属用户信息。

        :return: The user_id of this NovaKeypairDetail.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this NovaKeypairDetail.

        密钥所属用户信息。

        :param user_id: The user_id of this NovaKeypairDetail.
        :type: str
        """
        self._user_id = user_id

    @property
    def type(self):
        """Gets the type of this NovaKeypairDetail.

        密钥类型，默认“ssh”  微版本2.2以上支持

        :return: The type of this NovaKeypairDetail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NovaKeypairDetail.

        密钥类型，默认“ssh”  微版本2.2以上支持

        :param type: The type of this NovaKeypairDetail.
        :type: str
        """
        self._type = type

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
        if not isinstance(other, NovaKeypairDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other