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
