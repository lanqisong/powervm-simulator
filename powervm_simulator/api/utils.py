import sys

def read(f_name):
    base_dir = sys.path[0]
    with open("%s/data/%s" % (base_dir, f_name), "r") as fin:
        return ''.join(fin.readlines())
