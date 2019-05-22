## *********************************************************
##
## File autogenerated for the dynamic_reconfigure_test package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 245, 'name': 'Default', 'parent': 0, 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/src/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [{'upper': 'GROUP_ONE', 'lower': 'group_one', 'srcline': 124, 'name': 'Group_One', 'parent': 0, 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/src/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::GROUP_ONE', 'field': 'DEFAULT::group_one', 'state': True, 'parentclass': 'DEFAULT', 'groups': [{'upper': 'GROUP2', 'lower': 'group2', 'srcline': 124, 'name': 'GROUP2', 'parent': 1, 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/src/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'false', 'parentname': 'Group_One', 'class': 'DEFAULT::GROUP_ONE::GROUP2', 'field': 'DEFAULT::GROUP_ONE::group2', 'state': False, 'parentclass': 'DEFAULT::GROUP_ONE', 'groups': [{'upper': 'GROUP3', 'lower': 'group3', 'srcline': 124, 'name': 'Group3', 'parent': 2, 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/src/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'GROUP2', 'class': 'DEFAULT::GROUP_ONE::GROUP2::GROUP3', 'field': 'DEFAULT::GROUP_ONE::GROUP2::group3', 'state': True, 'parentclass': 'DEFAULT::GROUP_ONE::GROUP2', 'groups': [], 'parameters': [{'srcline': 70, 'description': 'Were very far down now', 'max': 3, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/cfg/Test.cfg', 'name': 'deep_var_int', 'edit_method': "{'enum_description': 'An enum to set the size.', 'enum': [{'srcline': 45, 'description': 'A small constant', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/cfg/Test.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'Small'}, {'srcline': 46, 'description': 'A medium value', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/cfg/Test.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'Medium'}, {'srcline': 47, 'description': 'A large value', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/cfg/Test.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'Large'}, {'srcline': 48, 'description': 'An extra large value', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/cfg/Test.cfg', 'cconsttype': 'const int', 'value': 3, 'ctype': 'int', 'type': 'int', 'name': 'ExtraLarge'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 71, 'description': 'Were even farther down now!!', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/cfg/Test.cfg', 'name': 'deep_var_bool', 'edit_method': '', 'default': True, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 72, 'description': 'Were super far down now!!', 'max': inf, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/cfg/Test.cfg', 'name': 'deep_var_double', 'edit_method': '', 'default': -1.0, 'level': 0, 'min': -inf, 'type': 'double'}], 'type': '', 'id': 3}], 'parameters': [{'srcline': 65, 'description': 'A third level group parameter', 'max': inf, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/cfg/Test.cfg', 'name': 'group2_double', 'edit_method': '', 'default': 3.333, 'level': 0, 'min': -inf, 'type': 'double'}, {'srcline': 66, 'description': 'A third level group parameter', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/cfg/Test.cfg', 'name': 'group2_string', 'edit_method': '', 'default': 'test string', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 67, 'description': 'Something', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/cfg/Test.cfg', 'name': 'some_other', 'edit_method': '', 'default': 'AAAAAAGGHH', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 68, 'description': 'A boolean', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/cfg/Test.cfg', 'name': 'variable', 'edit_method': '', 'default': True, 'level': 0, 'min': False, 'type': 'bool'}], 'type': 'collapse', 'id': 2}], 'parameters': [{'srcline': 63, 'description': 'A second level group parameter', 'max': 2147483647, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/cfg/Test.cfg', 'name': 'group1_int', 'edit_method': '', 'default': 2, 'level': 1, 'min': -2147483648, 'type': 'int'}], 'type': '', 'id': 1}, {'upper': 'UPPER_GROUP_2', 'lower': 'upper_group_2', 'srcline': 124, 'name': 'Upper_Group_2', 'parent': 0, 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/src/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::UPPER_GROUP_2', 'field': 'DEFAULT::upper_group_2', 'state': True, 'parentclass': 'DEFAULT', 'groups': [], 'parameters': [{'srcline': 75, 'description': 'Some param', 'max': 2147483647, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/cfg/Test.cfg', 'name': 'some_param', 'edit_method': '', 'default': 20, 'level': 0, 'min': -2147483648, 'type': 'int'}], 'type': '', 'id': 4}], 'parameters': [{'srcline': 290, 'description': 'Int enum', 'max': 3, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/src/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'int_enum_', 'edit_method': "{'enum_description': 'An enum to set the size.', 'enum': [{'srcline': 45, 'description': 'A small constant', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/cfg/Test.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'Small'}, {'srcline': 46, 'description': 'A medium value', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/cfg/Test.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'Medium'}, {'srcline': 47, 'description': 'A large value', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/cfg/Test.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'Large'}, {'srcline': 48, 'description': 'An extra large value', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/cfg/Test.cfg', 'cconsttype': 'const int', 'value': 3, 'ctype': 'int', 'type': 'int', 'name': 'ExtraLarge'}]}", 'default': 0, 'level': 1, 'min': 0, 'type': 'int'}, {'srcline': 290, 'description': 'Int parameter', 'max': 10, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/src/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'int_', 'edit_method': '', 'default': 0, 'level': 1, 'min': -10, 'type': 'int'}, {'srcline': 290, 'description': 'double parameter', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/src/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'double_', 'edit_method': '', 'default': 0.0, 'level': 2, 'min': -2.0, 'type': 'double'}, {'srcline': 290, 'description': 'double parameter without boundaries', 'max': inf, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/src/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'double_no_minmax', 'edit_method': '', 'default': 1.0, 'level': 2, 'min': -inf, 'type': 'double'}, {'srcline': 290, 'description': 'double parameter without max value', 'max': inf, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/src/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'double_no_max', 'edit_method': '', 'default': 2.0, 'level': 2, 'min': 0.0, 'type': 'double'}, {'srcline': 290, 'description': 'String parameter', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/src/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'str_', 'edit_method': '', 'default': 'foo', 'level': 4, 'min': '', 'type': 'str'}, {'srcline': 290, 'description': 'Multibyte String parameter', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/src/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'mstr_', 'edit_method': '', 'default': 'bar', 'level': 4, 'min': '', 'type': 'str'}, {'srcline': 290, 'description': 'Boolean parameter', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/src/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'bool_', 'edit_method': '', 'default': False, 'level': 8, 'min': False, 'type': 'bool'}, {'srcline': 290, 'description': 'Contains the level of the previous change', 'max': 2147483647, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/src/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'level', 'edit_method': '', 'default': 0, 'level': 16, 'min': -2147483648, 'type': 'int'}, {'srcline': 290, 'description': 'Checks against regression of #4499', 'max': 2147483647, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/src/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'int_nodefault', 'edit_method': '', 'default': 0, 'level': 0, 'min': -2147483648, 'type': 'int'}, {'srcline': 290, 'description': 'Checks against regression of https://github.com/ros/dynamic_reconfigure/issues/6', 'max': 2147483647, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/tmp/binarydeb/ros-indigo-dynamic-reconfigure-1.5.50/src/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'i', 'edit_method': '', 'default': 0, 'level': 0, 'min': -2147483648, 'type': 'int'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

Test_int_const = 5
Test_double_const = 5.6
Test_str_const = 'foo'
Test_bool_const = True
Test_Small = 0
Test_Medium = 1
Test_Large = 2
Test_ExtraLarge = 3