def my_logger(func):
    import logging
    logging.basicConfig(filename = '{}.log'.format(func.__name__), level = logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info('Ran with args : {} and kwargs : {}'.format(args, kwargs))
        return func(*args, **kwargs)

    return wrapper

def my_timer(func):
    import time
    def wrapper(*args, **kwargs):
        t_start = time.time()
        result = func(*args, **kwargs)
        t_end = time.time() - t_start
        print('{} ran in : {} sec'.format(func.__name__, t_end))
        return result
    return wrapper

@my_logger
@my_timer
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Mrinal', 25)