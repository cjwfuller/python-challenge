import sys
import pickle

banner = open('banner.p', 'r')
b = pickle.load(banner)
banner.close

for line in b:
    for tup in line:
        for x in range(0, tup[1]):
            sys.stdout.write(str(tup[0]))
    print ""
