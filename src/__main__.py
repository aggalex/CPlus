import sys
from src.rules.namespace.namespace_contents import NamespaceContents

def dump(obj):
    print(obj.match)

def main(args):
    for arg in args[1:]:
        with open(arg, 'r') as file:
            dump(NamespaceContents(file.read()))

if __name__ == "__main__":
    main(sys.argv)