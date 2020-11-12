import os
from pyls import arguments


def main():
    """ This is the main which is called when running pyls"""
    # Configure Arguments and set corresponding variables
    output = generate_output()
    print_output(output)

def generate_output() -> list:
    return os.listdir('.')
def print_output(output_list:list):
    for node in output_list:
        if not node.startswith('.'):
            print(node)
    
    
