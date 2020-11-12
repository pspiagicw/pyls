import os
from pyls import arguments


def main():
    """ This is the main which is called when running pyls"""
    # Parse the arguments 
    args = arguments.parse_arguments()
    # Configure Arguments and set corresponding variables
    output = generate_output(args.directory)
    print_output(output,True if args.all else False)

def generate_output(directory:str) -> list:
    return os.listdir(directory)
def print_output(output_list:list,hidden:bool=False):
    for node in output_list:
        if not node.startswith('.') or hidden:
            print(node)
    
    
