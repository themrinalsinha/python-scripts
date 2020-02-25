# YOUTUBE LINK: https://www.youtube.com/watch?v=W7Rv-km3ZuA

# # Function Wrapper:
# class function_wrapper(object):
#     def __init__(self, wrapped):
#         self.wrapped = wrapped
#
#     def __call__(self, *args, **kwargs):
#         return self.wrapped(*args, **kwargs)
#
# @function_wrapper
# def function():
#     pass
# =============================================
# # Doing work in the wrapper
# class function_wrapper(object):
#     def __init__(self, wrapped):
#         self.wrapped = wrapped
#
#     def __call__(self, *args, **kwargs):
#         name = self.wrapped.__name__
#         print('Enter %s()' % name)
#         try:
#             return self.wrapped(*args, **kwargs)
#         finally:
#             print('exit %s()' % name)
#
# @function_wrapper
# def function():
#     pass
# =============================================

class MyDecorator(object):
    def __init__(self):
        self.functions = []

    def rule(self, func):
        print(func.__name__)
        self.functions.append(func.__name__)
        return func

    def all_funcs(self):
        print(self.functions)


x = MyDecorator()


@x.rule
def hello():
    return

@x.rule
def world():
    return

@x.rule
def how():
    return

@x.rule
def are_you():
    return

x.all_funcs()
