from functools import partial, wraps

def background_task(method=None, queue='default', timeout=600):
    print('METHOD: ', method)
    if method is None:
        return partial(background_task, queue=queue, timeout=timeout)

    def start(a, b, **kwargs):
        print('\nstart function called')
        print('start -> A -> ', a)
        print('start -> B -> ', b)
        print('start -> kwargs -> ', kwargs)

    @wraps(method)
    def wrapper(*args, **kwargs):
        print('\nwrapper function called')
        print('wrapper -> args -> ', args)
        print('wrapper -> kwargs -> ', kwargs)
    wrapper.start = start
    return wrapper

@background_task()
def add(a, b):
    return a + b

print(add(12, 12))
print(add.start(12, 12))

