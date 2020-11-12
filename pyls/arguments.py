import argparse


def parse_arguments()->'Namespace':
    """ This method retures the namespace object after parsing arguments"""
    parser = argparse.ArgumentParser(description='Pure python clone of ls command')
    parser.add_argument('directory',metavar='Directory',default='.',help='The directory name to print the contents on.',nargs='?',type=str)
    return parser.parse_args()


