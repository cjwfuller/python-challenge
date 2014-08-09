nothing = '90052'
while True:
    f = open('channel/' + nothing + '.txt', 'r')
    line = f.readline()
    splits = line.split('Next nothing is ', 1)
    if(len(splits) == 2):
        nothing = splits[1]
        print nothing
    else:
        break
