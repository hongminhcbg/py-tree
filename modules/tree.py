import os
import subprocess
def get_abs_path(current, relative):
    if relative != './':
        return current + relative
    
    return current

def parser_single_line(line):
    ignore_list = {'.git', '.gitignore', '.', '..'}

    args = line.split(" ")
    if len(args) != 9:
        return None
    
    if args[8] in ignore_list:
        return None

    result = {}
    result["is_dir"] = args[0].startswith('d')
    result["name"] = args[8]
    return result

def parse_output_ls_to_dist(raw_string):
    
    for line in raw_string.splitlines():
        #print(f'line = {line}')
        obj = parser_single_line(line)
        print(f'type of object is {type(obj)}, value is {obj}')

def tree(argv):
    print(f'[DB] current dir = {os.getcwd()}')
    print(f'[DB] relative dir = {argv[0]}')
    abs_dir = get_abs_path(os.getcwd(), argv[0])

    output = subprocess.getoutput(f'ls -lah {abs_dir}')
    print(f'[DB] output = {output}')
    parse_output_ls_to_dist(output)
