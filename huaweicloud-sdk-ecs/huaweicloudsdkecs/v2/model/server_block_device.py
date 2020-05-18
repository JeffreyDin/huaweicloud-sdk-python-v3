# coding: utf-8

import pprint
import re

import six


class ServerBlockDevice(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'boot_index': 'int',
        'pci_address': 'str',
        'volume_id': 'str',
        'device': 'str',
        'server_id': 'str',
        'id': 'str',
        'size': 'int',
        'bus': 'str'
    }

    attribute_map = {
        'boot_index': 'bootIndex',
        'pci_address': 'pciAddress',
        'volume_id': 'volumeId',
        'device': 'device',
        'server_id': 'serverId',
        'id': 'id',
        'size': 'size',
        'bus': 'bus'
    }

    def __init__(self, boot_index=None, pci_address=None, volume_id=None, device=None, server_id=None, id=None, size=None, bus=None):  # noqa: E501
        """ServerBlockDevice - a model defined in huaweicloud sdk"""

        self._boot_index = None
        self._pci_address = None
        self._volume_id = None
        self._device = None
        self._server_id = None
        self._id = None
        self._size = None
        self._bus = None
        self.discriminator = None

        if boot_index is not None:
            self.boot_index = boot_index
        if pci_address is not None:
            self.pci_address = pci_address
        if volume_id is not None:
            self.volume_id = volume_id
        if device is not None:
            self.device = device
        if server_id is not None:
            self.server_id = server_id
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if bus is not None:
            self.bus = bus

    @property
    def boot_index(self):
        """Gets the boot_index of this ServerBlockDevice.

        云硬盘启动顺序。  - 0为系统盘。  - 非0为数据盘

        :return: The boot_index of this ServerBlockDevice.
        :rtype: int
        """
        return self._boot_index

    @boot_index.setter
    def boot_index(self, boot_index):
        """Sets the boot_index of this ServerBlockDevice.

        云硬盘启动顺序。  - 0为系统盘。  - 非0为数据盘

        :param boot_index: The boot_index of this ServerBlockDevice.
        :type: int
        """
        self._boot_index = boot_index

    @property
    def pci_address(self):
        """Gets the pci_address of this ServerBlockDevice.

        pci地址。

        :return: The pci_address of this ServerBlockDevice.
        :rtype: str
        """
        return self._pci_address

    @pci_address.setter
    def pci_address(self, pci_address):
        """Sets the pci_address of this ServerBlockDevice.

        pci地址。

        :param pci_address: The pci_address of this ServerBlockDevice.
        :type: str
        """
        self._pci_address = pci_address

    @property
    def volume_id(self):
        """Gets the volume_id of this ServerBlockDevice.

        云硬盘ID，UUID格式。

        :return: The volume_id of this ServerBlockDevice.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this ServerBlockDevice.

        云硬盘ID，UUID格式。

        :param volume_id: The volume_id of this ServerBlockDevice.
        :type: str
        """
        self._volume_id = volume_id

    @property
    def device(self):
        """Gets the device of this ServerBlockDevice.

        云硬盘挂载盘符，即磁盘挂载点。

        :return: The device of this ServerBlockDevice.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this ServerBlockDevice.

        云硬盘挂载盘符，即磁盘挂载点。

        :param device: The device of this ServerBlockDevice.
        :type: str
        """
        self._device = device

    @property
    def server_id(self):
        """Gets the server_id of this ServerBlockDevice.

        弹性云服务器ID，UUID格式。

        :return: The server_id of this ServerBlockDevice.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this ServerBlockDevice.

        弹性云服务器ID，UUID格式。

        :param server_id: The server_id of this ServerBlockDevice.
        :type: str
        """
        self._server_id = server_id

    @property
    def id(self):
        """Gets the id of this ServerBlockDevice.

        挂载ID，与云硬盘ID相同。UUID格式。

        :return: The id of this ServerBlockDevice.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ServerBlockDevice.

        挂载ID，与云硬盘ID相同。UUID格式。

        :param id: The id of this ServerBlockDevice.
        :type: str
        """
        self._id = id

    @property
    def size(self):
        """Gets the size of this ServerBlockDevice.

        云硬盘大小，单位GB。

        :return: The size of this ServerBlockDevice.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ServerBlockDevice.

        云硬盘大小，单位GB。

        :param size: The size of this ServerBlockDevice.
        :type: int
        """
        self._size = size

    @property
    def bus(self):
        """Gets the bus of this ServerBlockDevice.

        磁盘总线类型 。  取值范围：virtio、scsi

        :return: The bus of this ServerBlockDevice.
        :rtype: str
        """
        return self._bus

    @bus.setter
    def bus(self, bus):
        """Sets the bus of this ServerBlockDevice.

        磁盘总线类型 。  取值范围：virtio、scsi

        :param bus: The bus of this ServerBlockDevice.
        :type: str
        """
        self._bus = bus

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
        if not isinstance(other, ServerBlockDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other