'''
robert.anderson@kcl.ac.uk

rosbench, when invoked on a directory containing the requisite assets, will launch an instance
of a program, and report various statistics about that instance.

a conforming directory would include:
    - a run script (run.sh)
    - a getter python script for each statistic (get_<statname>.py)

the main() method is called in each getter.
a launch script (launch.sh) is optional, if it is absent the standard launch line:
    bash run.sh &

is assumed. Under cluster systems which use Slurm for example, the launch script may contain:
    sbatch run.sh
and under Sun Grid engine, the equivalent might be
    qsub run.sh

run.sh is modified with a footer which calls the getters and updates the rosbench.results.<index>
file in the source directory via the analyse.py module file.

any other contents will be copied to the temporary directory
'''

from common import *

print('Retrieving the following stats and information:')
for stat in statnames:
    print('\t"{}"'.format(stat))

assert src_exists('run.sh'), 'Source directory must contain run.sh'

if tmp_exists('.'): 
    print('Removing old temporary directory')
    shutil.rmtree(tmp_dir)
os.makedirs(tmp_dir)

'''
copy assets into tmp dir
'''
no_copy_paths = statpaths + [src_path('run.sh')]

for fname in glob(src_path('*')):
    if os.path.isdir(fname) or fname in no_copy_paths: continue
    shutil.copy(fname, tmp_path(os.path.basename(fname)))

'''
write run.sh with footer to conduct analysis upon completion
'''
with open(src_path('run.sh'), 'r') as fin, open(tmp_path('run.sh'), 'w') as fout:
    fout.write(''.join(fin.readlines()))
    fout.write('python {} {}'.format(mod_path('analyse.py'), src_dir))

'''
write default launch script if not supplied in src_dir
'''
if not tmp_exists('launch.sh'):
    with open(tmp_path('launch.sh'), 'w') as f: f.write(default_launch)

