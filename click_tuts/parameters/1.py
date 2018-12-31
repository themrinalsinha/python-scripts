# # Parameters:

# # Click supports two types of parameters for scripts: 'options' and 'arguments'
# # There is generally some confusion among authors of command line scripts of when
# # to use which, so optional. while arguments can be optional within reason.

# # Differences:
# # Arguments can do less than options. The following features are only available for options.
# #   -> Automatic prompting for missing input.
# #   -> Act as flag (boolean or otherwise)
# #   -> Option values can pulled from environment variables, arguments can no
# #   -> Options are fully documeted in the help page, arguments are not (this is
# #   intentional as arguments might be too specific to be automically documentd)

# # Parameter Types
# # str / click.STRING - The default parameter type which indicates unicode strings.
# # int / click.INT    - the parameter only accepts integers.
# # float / click.FLOAT - the parameter only accepts floating point values.
# # bool / click.BOOL - A parameter that accepts boolean values. This is automatically used for boolean flags.
# #                     if used with string value 1, yes, y, t and true convert True and 0, no, n, f and flase conver to False.
# # click.UUID: a parameter that accepts UUID values, This is not automatically.
# # class click.File(mode='r', encoding=None, errors='strict', lazy = None, atomic=False)
#     # Declares a parameter to be a file for reading or writing. the fine is automatically close one tht context tears down.
# # class click.Path(exists=False, file_okay=True, dir_okay=True, writable=False....)...

# Parameter Types
# Parameters can be of different types. Types can be implemented with different behavior and some are supported out of the box:

# str / click.STRING:
# The default parameter type which indicates unicode strings.

# int / click.INT:
# A parameter that only accepts integers.

# float / click.FLOAT:
# A parameter that only accepts floating point values.

# bool / click.BOOL:
# A parameter that accepts boolean values. This is automatically used for boolean flags. If used with string values 1, yes, y, t and true convert to True and 0, no, n, f and false convert to False.

# click.UUID:
# A parameter that accepts UUID values. This is not automatically guessed but represented as uuid.UUID.

# class click.File(mode='r', encoding=None, errors='strict', lazy=None, atomic=False)
# Declares a parameter to be a file for reading or writing. The file is automatically closed once the context tears down (after the command finished working).

# Files can be opened for reading or writing. The special value - indicates stdin or stdout depending on the mode.

# By default, the file is opened for reading text data, but it can also be opened in binary mode or for writing. The encoding parameter can be used to force a specific encoding.

# The lazy flag controls if the file should be opened immediately or upon first IO. The default is to be non-lazy for standard input and output streams as well as files opened for reading, lazy otherwise. When opening a file lazily for reading, it is still opened temporarily for validation, but will not be held open until first IO. lazy is mainly useful when opening for writing to avoid creating the file until it is needed.

# Starting with Click 2.0, files can also be opened atomically in which case all writes go into a separate file in the same folder and upon completion the file will be moved over to the original location. This is useful if a file regularly read by other users is modified.

# See File Arguments for more information.

# class click.Path(exists=False, file_okay=True, dir_okay=True, writable=False, readable=True, resolve_path=False, allow_dash=False, path_type=None)
# The path type is similar to the File type but it performs different checks. First of all, instead of returning an open file handle it returns just the filename. Secondly, it can perform various basic checks about what the file or directory should be.

# Changed in version 6.0: allow_dash was added.

# Parameters
# exists – if set to true, the file or directory needs to exist for this value to be valid. If this is not required and a file does indeed not exist, then all further checks are silently skipped.

# file_okay – controls if a file is a possible value.

# dir_okay – controls if a directory is a possible value.

# writable – if true, a writable check is performed.

# readable – if true, a readable check is performed.

# resolve_path – if this is true, then the path is fully resolved before the value is passed onwards. This means that it’s absolute and symlinks are resolved. It will not expand a tilde-prefix, as this is supposed to be done by the shell only.

# allow_dash – If this is set to True, a single dash to indicate standard streams is permitted.

# path_type – optionally a string type that should be used to represent the path. The default is None which means the return value will be either bytes or unicode depending on what makes most sense given the input data Click deals with.

# class click.Choice(choices, case_sensitive=True)
# The choice type allows a value to be checked against a fixed set of supported values. All of these values have to be strings.

# You should only pass a list or tuple of choices. Other iterables (like generators) may lead to surprising results.

# See Choice Options for an example.

# Parameters
# case_sensitive – Set to false to make choices case insensitive. Defaults to true.

# class click.IntRange(min=None, max=None, clamp=False)
# A parameter that works similar to click.INT but restricts the value to fit into a range. The default behavior is to fail if the value falls outside the range, but it can also be silently clamped between the two edges.

# See Range Options for an example.

# class click.FloatRange(min=None, max=None, clamp=False)
# A parameter that works similar to click.FLOAT but restricts the value to fit into a range. The default behavior is to fail if the value falls outside the range, but it can also be silently clamped between the two edges.

# See Range Options for an example.

# class click.DateTime(formats=None)
# The DateTime type converts date strings into datetime objects.

# The format strings which are checked are configurable, but default to some common (non-timezone aware) ISO 8601 formats.

# When specifying DateTime formats, you should only pass a list or a tuple. Other iterables, like generators, may lead to surprising results.

# The format strings are processed using datetime.strptime, and this consequently defines the format strings which are allowed.

# Parsing is tried using each format, in order, and the first format which parses successfully is used.

# Parameters
# formats – A list or tuple of date format strings, in the order in which they should be tried. Defaults to '%Y-%m-%d', '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M:%S'.

# Custom parameter types can be implemented by subclassing click.ParamType. For simple cases, passing a Python function that fails with a ValueError is also supported, though discouraged.

# Parameter Names
# Parameters (both options and arguments) accept a number of positional arguments which are passed to the command function as parameters. Each string with a single dash is added as a short argument; each string starting with a double dash as a long one.

# If a string is added without any dashes, it becomes the internal parameter name which is also used as variable name.

# If all names for a parameter contain dashes, the internal name is generated automatically by taking the longest argument and converting all dashes to underscores.

# The internal name is converted to lowercase.

# Examples:

# For an option with ('-f', '--foo-bar'), the parameter name is foo_bar.

# For an option with ('-x',), the parameter is x.

# For an option with ('-f', '--filename', 'dest'), the parameter name is dest.

# For an option with ('--CamelCaseOption',), the parameter is camelcaseoption.

# For an arguments with (`foogle`), the parameter name is foogle. To provide a different human readable name for use in help text, see the section about Truncating Help Texts.

# Implementing Custom Types
# To implement a custom type, you need to subclass the ParamType class. Types can be invoked with or without context and parameter object, which is why they need to be able to deal with this.

# The following code implements an integer type that accepts hex and octal numbers in addition to normal integers, and converts them into regular integers:

# import click

# class BasedIntParamType(click.ParamType):
#     name = 'integer'

#     def convert(self, value, param, ctx):
#         try:
#             if value[:2].lower() == '0x':
#                 return int(value[2:], 16)
#             elif value[:1] == '0':
#                 return int(value, 8)
#             return int(value, 10)
#         except ValueError:
#             self.fail('%s is not a valid integer' % value, param, ctx)

# BASED_INT = BasedIntParamType()
# As you can see, a subclass needs to implement the ParamType.convert() method and optionally provide the ParamType.name attribute. The latter can be used for documentation purposes.
