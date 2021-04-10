#import shutil
import sys

#file1 = open(sys.argv[1], 'r')
#copy = open(sys.argv[2], 'wt')
#line = file1.read()
#copy.write(str(line))
#file1.close()
#copy.close()

with open(sys.argv[1], 'r') as input:
    with open(sys.argv[2], 'wt') as output:
        output.write(input.read())