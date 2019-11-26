#!/usr/bin/env python3

import csv
import sys

input_file = sys.argv[1] 
output_file = sys.argv[2] 

csv.register_dialect('pipes', delimiter='|')

with open(input_file, 'rt') as f1, open(output_file, 'wt') as f2:
    
    reader = csv.reader(f1,dialect='pipes')
    writer = csv.writer(f2)

    for row in reader:
        print(row)
        writer.writerow(row)
    
