import argparse
parser = argparse.ArgumentParser()
parser.add_argument('start', help='Starting value', type=int) #positional parameter
parser.add_argument('end', help='Ending value (inclusive by default)', type=int)
#flag
parser.add_argument('-x', '--exclusive', help='Ending value is exclusive', action='store_const', const=0, dest='end_delta')
#options
parser.add_argument('--step', help='Step', default=1, type=int)

args = parser.parse_args()
start = args.start
end = args.end + args.end_delta
step = args.step

for i in range(start, end, step):
    print(i)