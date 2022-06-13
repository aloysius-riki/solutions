"""
Python script to combine multiple JSON files into one."""

import sys
import pandas as pd
import os
import glob
    

def combine_json_files(my_dir, output_file):

    end, n = (']\n', ',\n'), len(my_dir)

    with open(output_file, 'w') as o:
        o.write('[')
        for infile in my_dir:
            n -= 1
            with open(infile, 'r') as i:
                o.write(i.read().strip() + end[n>0]) # select correct end separator

def main(my_dir):
    """
    Combine multiple JSON files into one.
    """

    # Combine all JSON files into one.
    combine_json_files(my_dir, 'combined_json.json')
    

if __name__ == '__main__':
    # hard code the directory
    # my_dir = os.listdir("/path/to/json/files")
    # or pass the directory as an argument
    my_dir = os.listdir(sys.argv[1])
    
    main(my_dir) 