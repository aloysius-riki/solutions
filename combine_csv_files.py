"""
Python script to combine multiple CSV files into one."""

import sys
import pandas as pd
import os
import glob
    

def combine_csv_files(my_dir, output_file):

    #set working directory
    os.chdir(my_dir)

    #find all csv files in the folder
    #use glob pattern matching -> extension = 'csv'
    #save result in list -> all_filenames
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    #print(all_filenames)

    #combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
    #export to csv
    combined_csv.to_csv( output_file, index=False, encoding='utf-8-sig')

def main(my_dir):
    """
    Combine multiple CSV files into one.
    """
    output_file = 'combined_csv.csv'
    # Combine all CSV files into one.
    combine_csv_files(my_dir, output_file)
    

if __name__ == '__main__':
    # get directory from command line argument
    my_dir = sys.argv[1]
    # or hard code directory
    # smy_dir = "/path/to/csv/directory"
    main(my_dir) 