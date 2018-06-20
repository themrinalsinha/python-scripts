class CleanCode(object):
    def __init__(self, txtfile):
        self.txtfile = txtfile

    def clean(self):
        with open(self.txtfile, 'r') as f:
            for line in f.readlines():
                line = line.strip().split(' ')[2:]
                yield ' '.join(l for l in line)

    @property
    def code(self):
        return [x for x in self.clean()]

class ParseFortran(object):
    def __init__(self, code):
        self.code = code

    def keywords(self):
        return [x.strip() for x in self.code if not x.startswith(' ')\
                or len(x.strip().split(',')) is 1]

    @property
    def groupkey(self):
        initial     = 0
        groups      = {}
        self.code_w = [x.strip() for x in self.code]
        for initial in range(len(self.keywords()) - 1):
            groups.setdefault(self.keywords()[initial], [])
            for x in range(self.code_w.index(self.keywords()[initial]) + 1, \
                           self.code_w.index(self.keywords()[initial + 1])):
                groups[self.keywords()[initial]].append(self.code_w[x])
        return groups

    def contentkey(self):
        contents = {}
        data     = {}
        for keyword in self.keywords()[:-1]:
            contents.setdefault(keyword, [])
            for x in self.groupkey.get(keyword):
                x = x.strip().split(',')
                data.setdefault(x[0], [])
                data[x[0]].append(x[-1])
            contents[keyword].append(data)
        return contents

code   = CleanCode('sample.txt')
result = ParseFortran(code.code)
print(result.contentkey())
