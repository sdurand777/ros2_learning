# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ros2_learning_msg:srv/SetCommand.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'parameters'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_SetCommand_Request(type):
    """Metaclass of message 'SetCommand_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'CMD_ARM': 0,
        'CMD_DISARM': 1,
        'CMD_SET_MODE': 2,
        'CMD_SET_DEPTH': 3,
        'CMD_SET_HEADING': 4,
        'CMD_MOVE': 5,
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
                'ros2_learning_msg.srv.SetCommand_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__set_command__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__set_command__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__set_command__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__set_command__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__set_command__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'CMD_ARM': cls.__constants['CMD_ARM'],
            'CMD_DISARM': cls.__constants['CMD_DISARM'],
            'CMD_SET_MODE': cls.__constants['CMD_SET_MODE'],
            'CMD_SET_DEPTH': cls.__constants['CMD_SET_DEPTH'],
            'CMD_SET_HEADING': cls.__constants['CMD_SET_HEADING'],
            'CMD_MOVE': cls.__constants['CMD_MOVE'],
        }

    @property
    def CMD_ARM(self):
        """Message constant 'CMD_ARM'."""
        return Metaclass_SetCommand_Request.__constants['CMD_ARM']

    @property
    def CMD_DISARM(self):
        """Message constant 'CMD_DISARM'."""
        return Metaclass_SetCommand_Request.__constants['CMD_DISARM']

    @property
    def CMD_SET_MODE(self):
        """Message constant 'CMD_SET_MODE'."""
        return Metaclass_SetCommand_Request.__constants['CMD_SET_MODE']

    @property
    def CMD_SET_DEPTH(self):
        """Message constant 'CMD_SET_DEPTH'."""
        return Metaclass_SetCommand_Request.__constants['CMD_SET_DEPTH']

    @property
    def CMD_SET_HEADING(self):
        """Message constant 'CMD_SET_HEADING'."""
        return Metaclass_SetCommand_Request.__constants['CMD_SET_HEADING']

    @property
    def CMD_MOVE(self):
        """Message constant 'CMD_MOVE'."""
        return Metaclass_SetCommand_Request.__constants['CMD_MOVE']


class SetCommand_Request(metaclass=Metaclass_SetCommand_Request):
    """
    Message class 'SetCommand_Request'.

    Constants:
      CMD_ARM
      CMD_DISARM
      CMD_SET_MODE
      CMD_SET_DEPTH
      CMD_SET_HEADING
      CMD_MOVE
    """

    __slots__ = [
        '_robot_name',
        '_command_type',
        '_parameters',
    ]

    _fields_and_field_types = {
        'robot_name': 'string',
        'command_type': 'uint8',
        'parameters': 'sequence<float>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.robot_name = kwargs.get('robot_name', str())
        self.command_type = kwargs.get('command_type', int())
        self.parameters = array.array('f', kwargs.get('parameters', []))

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
        if self.command_type != other.command_type:
            return False
        if self.parameters != other.parameters:
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

    @builtins.property
    def command_type(self):
        """Message field 'command_type'."""
        return self._command_type

    @command_type.setter
    def command_type(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'command_type' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'command_type' field must be an unsigned integer in [0, 255]"
        self._command_type = value

    @builtins.property
    def parameters(self):
        """Message field 'parameters'."""
        return self._parameters

    @parameters.setter
    def parameters(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'f', \
                "The 'parameters' array.array() must have the type code of 'f'"
            self._parameters = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -3.402823466e+38 or val > 3.402823466e+38) or math.isinf(val) for val in value)), \
                "The 'parameters' field must be a set or sequence and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._parameters = array.array('f', value)


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_SetCommand_Response(type):
    """Metaclass of message 'SetCommand_Response'."""

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
                'ros2_learning_msg.srv.SetCommand_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__set_command__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__set_command__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__set_command__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__set_command__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__set_command__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SetCommand_Response(metaclass=Metaclass_SetCommand_Response):
    """Message class 'SetCommand_Response'."""

    __slots__ = [
        '_success',
        '_message',
        '_command_id',
    ]

    _fields_and_field_types = {
        'success': 'boolean',
        'message': 'string',
        'command_id': 'uint32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.success = kwargs.get('success', bool())
        self.message = kwargs.get('message', str())
        self.command_id = kwargs.get('command_id', int())

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
        if self.command_id != other.command_id:
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
    def command_id(self):
        """Message field 'command_id'."""
        return self._command_id

    @command_id.setter
    def command_id(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'command_id' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'command_id' field must be an unsigned integer in [0, 4294967295]"
        self._command_id = value


class Metaclass_SetCommand(type):
    """Metaclass of service 'SetCommand'."""

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
                'ros2_learning_msg.srv.SetCommand')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__set_command

            from ros2_learning_msg.srv import _set_command
            if _set_command.Metaclass_SetCommand_Request._TYPE_SUPPORT is None:
                _set_command.Metaclass_SetCommand_Request.__import_type_support__()
            if _set_command.Metaclass_SetCommand_Response._TYPE_SUPPORT is None:
                _set_command.Metaclass_SetCommand_Response.__import_type_support__()


class SetCommand(metaclass=Metaclass_SetCommand):
    from ros2_learning_msg.srv._set_command import SetCommand_Request as Request
    from ros2_learning_msg.srv._set_command import SetCommand_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
