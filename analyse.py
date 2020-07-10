from common import *
from datetime import datetime

i = len(glob(src_path('rosbench.results.*')))
with open(src_path('rosbench.results.{}'.format(i)), 'w') as f:
    time = datetime.now()
    f.write('#\n# RosBench results reported at {}\n#\n'.format(datetime.fromtimestamp(datetime.timestamp(time))))
    for statname, statfunc in zip(statnames, statfuncs):
        f.write('{}\n\t{}\n'.format(statname, statfunc()))
