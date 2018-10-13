class A():
    def __init__(self, a, aa):
        self.a  = a
        self.aa = aa

    def print_a(self):
        return self.a +' -- '+ self.aa

class B():
    def __init__(self, b, bb):
        self.b  = b
        self.bb = bb

    def print_b(self):
        return self.b +' || '+ self.bb

class C(A, B):
    def __init__(self, a, aa, b, bb, c, cc):
        A.__init__(self, a, aa)
        B.__init__(self, b, bb)
        self.c  = c
        self.cc = cc

    def print_c(self):
        return self.c +' ?? '+ self.cc

    def print_all(self):
        return self.print_a() +'|'+ self.print_b() + '|' + self.print_c()

if __name__ == '__main__':
    x = C('A', 'AA', 'B', 'BB', 'C', 'CC')

    print('Accessing class A : {}'.format(x.print_a()))
    print('Accessing class B : {}'.format(x.print_b()))
    print('Accessing class C : {}'.format(x.print_c()))
    print('Accessing all : {}'.format(x.print_all()))
    # a = A('A', 'AA')
    # print(a.print_a())

    # b = B('a', 'aa', 'b', 'bb')
    # print(b.print_b())
