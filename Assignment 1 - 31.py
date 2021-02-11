def filread(fname, nlines):
    from itertools import islice
    with open(fname) as f:
        for line in islice(f, nlines):
            print(line)

from Collections import counter
def word_count(fname):
    with open(fname) as f:
        return Counter(f.read().split())

fname = input("Enter the file name: ")
nlines = int(input("Enter the number of lines: "))             
filread(fname, nlines)
