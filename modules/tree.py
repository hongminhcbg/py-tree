import os
import subprocess
def get_abs_path(current, relative):
    if relative == './': 
        return current

    if relative.startswith('./'):
        return current + relative[1:]
    
    return current + relative

def parser_single_line(line):
    ignore_list = {'.git', '.gitignore', '.', '..'}

    args = line.split()
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
        obj = parser_single_line(line)
        print(f'type of object is {type(obj)}, value is {obj}')

def parse_abs_path_to_dict(abs_path):
    output = subprocess.getoutput(f'ls -lah {abs_path}')
    result = {}
    for line in output.splitlines():
        obj = parser_single_line(line)
        if obj is not None:
            if not obj.get('is_dir'):
                result[obj.get("name")] = True
                continue
            
            result[obj.get("name")] = parse_abs_path_to_dict(f'{abs_path}/{obj.get("name")}')
    return result

def display(prefix, dict_result):
    keys = dict_result.keys()
    for key in keys:
        print(f'{prefix}{key}')
        value = dict_result.get(key)
        if type(value) is bool:
            continue

        display(prefix+'--', value)

def tree(argv):
    print(f'[DB] current dir = {os.getcwd()}')
    print(f'[DB] relative dir = {argv[0]}')
    abs_dir = get_abs_path(os.getcwd(), argv[0])

    tree_result = parse_abs_path_to_dict(abs_path=abs_dir)
    print(tree_result)
    display('', tree_result)