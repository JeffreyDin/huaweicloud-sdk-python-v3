# coding: utf-8

import pprint
import re

import six


class NeutronCreateNetworkOption(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'name': 'str',
        'admin_state_up': 'bool',
        'providernetwork_type': 'str',
        'port_security_enabled': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'admin_state_up': 'admin_state_up',
        'providernetwork_type': 'provider:network_type',
        'port_security_enabled': 'port_security_enabled'
    }

    def __init__(self, name=None, admin_state_up=True, providernetwork_type=None, port_security_enabled=True):  # noqa: E501
        """NeutronCreateNetworkOption - a model defined in huaweicloud sdk"""

        self._name = None
        self._admin_state_up = None
        self._providernetwork_type = None
        self._port_security_enabled = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if providernetwork_type is not None:
            self.providernetwork_type = providernetwork_type
        if port_security_enabled is not None:
            self.port_security_enabled = port_security_enabled

    @property
    def name(self):
        """Gets the name of this NeutronCreateNetworkOption.

        功能说明：网络名称 取值范围：0-255个字符 约束：不能为admin_external_net

        :return: The name of this NeutronCreateNetworkOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronCreateNetworkOption.

        功能说明：网络名称 取值范围：0-255个字符 约束：不能为admin_external_net

        :param name: The name of this NeutronCreateNetworkOption.
        :type: str
        """
        self._name = name

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this NeutronCreateNetworkOption.

        功能说明：资源的管理状态 取值范围：true、false 约束：只支持true

        :return: The admin_state_up of this NeutronCreateNetworkOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this NeutronCreateNetworkOption.

        功能说明：资源的管理状态 取值范围：true、false 约束：只支持true

        :param admin_state_up: The admin_state_up of this NeutronCreateNetworkOption.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def providernetwork_type(self):
        """Gets the providernetwork_type of this NeutronCreateNetworkOption.

        功能说明：扩展属性：网络类型。管理员属性，普通租户不可见，允许 geneve类型租户执行操作。 取值范围：vxlan, geneve

        :return: The providernetwork_type of this NeutronCreateNetworkOption.
        :rtype: str
        """
        return self._providernetwork_type

    @providernetwork_type.setter
    def providernetwork_type(self, providernetwork_type):
        """Sets the providernetwork_type of this NeutronCreateNetworkOption.

        功能说明：扩展属性：网络类型。管理员属性，普通租户不可见，允许 geneve类型租户执行操作。 取值范围：vxlan, geneve

        :param providernetwork_type: The providernetwork_type of this NeutronCreateNetworkOption.
        :type: str
        """
        self._providernetwork_type = providernetwork_type

    @property
    def port_security_enabled(self):
        """Gets the port_security_enabled of this NeutronCreateNetworkOption.

        功能说明：端口安全使能标记 取值范围：true(启用)、false(禁用) 约束：如果不使能，则network下所有虚机的安全组和dhcp防欺骗不生效

        :return: The port_security_enabled of this NeutronCreateNetworkOption.
        :rtype: bool
        """
        return self._port_security_enabled

    @port_security_enabled.setter
    def port_security_enabled(self, port_security_enabled):
        """Sets the port_security_enabled of this NeutronCreateNetworkOption.

        功能说明：端口安全使能标记 取值范围：true(启用)、false(禁用) 约束：如果不使能，则network下所有虚机的安全组和dhcp防欺骗不生效

        :param port_security_enabled: The port_security_enabled of this NeutronCreateNetworkOption.
        :type: bool
        """
        self._port_security_enabled = port_security_enabled

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
        if not isinstance(other, NeutronCreateNetworkOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other