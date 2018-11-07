from os   import path, listdir
from sys  import argv
from glob import glob

class ProcessOrder(object):
    def __init__(self, basedir):
        self.basedir   = basedir
        self.order_no  = path.basename(path.dirname(self.basedir))
        self.zip_file  = ([x for x in glob(path.join(self.basedir, '*.zip'))
                            if 'failed.zip' not in x] or [None])[0]
        self.json_file = (glob(path.join(self.basedir, '*.json')) or [None])[0]
        self.mca_id    = path.basename(path.splitext(self.zip_file)[0])

if __name__ == '__main__':
    order_objects = [ProcessOrder(path.join(argv[1], x)) \
                    for x in listdir(argv[1]) if x and x.startswith('O')]

    for order in order_objects:
        print(order.mca_id)
