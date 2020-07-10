

def main():
    import os
    from subprocess import Popen, PIPE
    os.chdir(os.environ['PROJECT_ROOT'])
    stdout, stderr = Popen('git rev-parse --short HEAD', shell=1, stdout=PIPE, stderr=PIPE).communicate()
    return str(stdout, 'utf8').strip()
