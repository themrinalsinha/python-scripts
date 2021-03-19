from tqdm import tqdm
import cProfile, pstats, io
from pstats import SortKey

def _hell(i, j, k):
    cal = i + j + k

def hello():
    for i in range(10):
        for j in range(20):
            for k in range(30):
                _hell(i, j, k)

pr = cProfile.Profile()
pr.enable()

hello()

pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
pr.dump_stats('sample.profile')
