import pstats

def f8(x):
    ret = "%8.3f" % x
    if ret != '   0.000':
        return ret
    return "%6dµs" % (x * 10000000)

pstats.f8 = f8

sts = pstats.Stats('main.prof')
sts.strip_dirs().sort_stats(-1).print_stats()
