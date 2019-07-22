# All about walrun operator: https://www.python.org/dev/peps/pep-0572/

# # Assignment Expression :=
#     # It is also known as walrus operator.
#     # It assigns values to variables as part of an expression without the need to initialise the variables up front.

# # earlier
# if get_input():
#     my_variable = get_input()
#     if my_variable is not None:
#         print(my_variable)
#         perform_action(my_variable)

# # python3.8
# if (my_variable := get_input()) is not None:
#     print(my_variable) # exists now
#     perform_action(my_variable)

# # This feature if available in list comprehensions and statement forms.
# # There are some important points to note. Firstly, ensure the assignment
# # of the variable is parenthesized. Unparenthesized assignment expressions
# # are prohibited at the top level of an expression statement:

# my_variable := get_input()   # invalid
# (my_variable := get_input()) # valid but it is not recommended

# # secondly, = and := are not the same, and the priority around the commons is different

# my_variable = a, b, c     # Sets my_variable to (a, b, c)
# (my_variable := a, b, c)  # Sets my_variable to a
