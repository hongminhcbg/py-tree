import os
import subprocess
def get_abs_path(current, relative):
    if relative != './':
        return current + relative
    
    return current

def tree(argv):
    print(f'[DB] current dir = {os.getcwd()}')
    print(f'[DB] relative dir = {argv[0]}')
    abs_dir = get_abs_path(os.getcwd(), argv[0])

    output = subprocess.getoutput(f'ls -lah {abs_dir}')
    print(f'[DB] output = {output}')
