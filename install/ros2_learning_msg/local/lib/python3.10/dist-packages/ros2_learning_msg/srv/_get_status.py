# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ros2_learning_msg:srv/GetStatus.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_GetStatus_Request(type):
    """Metaclass of message 'GetStatus_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('ros2_learning_msg')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'ros2_learning_msg.srv.GetStatus_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__get_status__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__get_status__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__get_status__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__get_status__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__get_status__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class GetStatus_Request(metaclass=Metaclass_GetStatus_Request):
    """Message class 'GetStatus_Request'."""

    __slots__ = [
        '_robot_name',
    ]

    _fields_and_field_types = {
        'robot_name': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.robot_name = kwargs.get('robot_name', str())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.robot_name != other.robot_name:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def robot_name(self):
        """Message field 'robot_name'."""
        return self._robot_name

    @robot_name.setter
    def robot_name(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'robot_name' field must be of type 'str'"
        self._robot_name = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_GetStatus_Response(type):
    """Metaclass of message 'GetStatus_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('ros2_learning_msg')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'ros2_learning_msg.srv.GetStatus_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__get_status__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__get_status__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__get_status__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__get_status__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__get_status__response

            from ros2_learning_msg.msg import RobotStatus
            if RobotStatus.__class__._TYPE_SUPPORT is None:
                RobotStatus.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class GetStatus_Response(metaclass=Metaclass_GetStatus_Response):
    """Message class 'GetStatus_Response'."""

    __slots__ = [
        '_success',
        '_message',
        '_status',
    ]

    _fields_and_field_types = {
        'success': 'boolean',
        'message': 'string',
        'status': 'ros2_learning_msg/RobotStatus',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ros2_learning_msg', 'msg'], 'RobotStatus'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.success = kwargs.get('success', bool())
        self.message = kwargs.get('message', str())
        from ros2_learning_msg.msg import RobotStatus
        self.status = kwargs.get('status', RobotStatus())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.success != other.success:
            return False
        if self.message != other.message:
            return False
        if self.status != other.status:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def success(self):
        """Message field 'success'."""
        return self._success

    @success.setter
    def success(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'success' field must be of type 'bool'"
        self._success = value

    @builtins.property
    def message(self):
        """Message field 'message'."""
        return self._message

    @message.setter
    def message(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'message' field must be of type 'str'"
        self._message = value

    @builtins.property
    def status(self):
        """Message field 'status'."""
        return self._status

    @status.setter
    def status(self, value):
        if __debug__:
            from ros2_learning_msg.msg import RobotStatus
            assert \
                isinstance(value, RobotStatus), \
                "The 'status' field must be a sub message of type 'RobotStatus'"
        self._status = value


class Metaclass_GetStatus(type):
    """Metaclass of service 'GetStatus'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('ros2_learning_msg')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'ros2_learning_msg.srv.GetStatus')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__get_status

            from ros2_learning_msg.srv import _get_status
            if _get_status.Metaclass_GetStatus_Request._TYPE_SUPPORT is None:
                _get_status.Metaclass_GetStatus_Request.__import_type_support__()
            if _get_status.Metaclass_GetStatus_Response._TYPE_SUPPORT is None:
                _get_status.Metaclass_GetStatus_Response.__import_type_support__()


class GetStatus(metaclass=Metaclass_GetStatus):
    from ros2_learning_msg.srv._get_status import GetStatus_Request as Request
    from ros2_learning_msg.srv._get_status import GetStatus_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
