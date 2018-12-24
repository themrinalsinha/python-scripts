class ToDictMixin(object):
    def to_dict(self):
        return self.__dict__

    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output

    def _traverse(self, key, value):
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        else:
            return value


class A(ToDictMixin):
    def __init__(self):
        self.name = 'Mrinal'
        self.post = 'Developer'

x = A()
print(x.to_dict())
