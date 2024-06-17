import logging
import os
from pprint import pprint
from pathlib import Path

logging.basicConfig(filename='todayslog.txt', level = logging.WARNING,  format = ' %(asctime)s -  %(levelname)s - %(message)s')

def get_base_path(): 
    current =  Path.cwd()
    assert isinstance(current, Path), 'Path is not a path'
    return current

my_csv = get_base_path() / 'customers-100.csv'
logging.warning('Some info about our current working directory', my_csv)

print(my_csv)
pprint(os.listdir(Path.cwd().parent))

def read_csv(filepath):
    list_employees = []
    try:
        with open(filepath, 'r') as file:
            for line in file:
                list_employees.append(line)
    except FileNotFoundError:
        print('Check the filename please')
    return list_employees

my_emps = read_csv(my_csv)
pprint(my_emps)
