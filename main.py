#!/user/bin/python3
import sys
from modules import version
from modules import help_func
from modules import tree


def main(argv):
    witcher = {
      '--version': version.version,
      '-v': version.version,
      '--help': help_func.help_func,
      '-h': help_func.help_func, 
    }

    func = witcher.get(argv[0], tree.tree)
    func(argv)

if __name__ == "__main__":
   main(sys.argv[1:])