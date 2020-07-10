import os, sys, shutil
from glob import glob
import importlib

mod_dir = os.path.abspath(os.path.dirname(__file__))
src_dir = os.path.abspath(sys.argv[1] if len(sys.argv)>1 else '.')
tmp_dir = os.path.abspath(src_dir+'/rosbench')

mod_path = lambda fname : os.path.abspath(mod_dir+'/'+fname)
src_path = lambda fname : os.path.abspath(src_dir+'/'+fname)
src_exists = lambda fname : os.path.exists(src_path(fname))
tmp_path = lambda fname : os.path.abspath(tmp_dir+'/'+fname)
tmp_exists = lambda fname : os.path.exists(tmp_path(fname))

stat_path = lambda name : src_path('get_'+name+'.py')

default_launch = 'bash run.sh &'

statpaths = glob(src_path('get_*.py'))
statnames = sorted([os.path.basename(match)[4:-3] for match in statpaths])

sys.path.append(src_dir)
statfuncs = []
for stat in statnames:
    modname = 'get_'+stat
    tmp = importlib.import_module(modname)
    statfuncs.append(getattr(tmp, 'main'))
