"""
A simple script to create a sample from a csv file

Copies every nth line of the csv to a new file.
"""

infile = "infile.csv"
outfile = "outfile_sample.csv"
skip = 500 # output at every 'skip' line

with open(infile, 'r') as inf, open(outfile, 'a') as ouf:
    a = inf.readlines()
    for i in range(0, len(a), skip):
        ouf.write(a[i])
