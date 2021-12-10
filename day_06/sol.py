import numpy as np

with open('input.txt', 'r') as fp:
    lines = [line.strip() for line in fp.readlines()]

initial_fish = [int(el) for el in lines[0].split(',')]

fish = initial_fish.copy()


do_part_one = True
do_part_two = True

if do_part_one:
    for iday in range(1,80+1):
        next_fish = []
        new_fish = []
        for ii in range(len(fish)):
            if fish[ii] == 0:
                next_fish.append(6)
                new_fish.append(8)
            else:
                next_fish.append(fish[ii] - 1)
        fish = next_fish.copy() + new_fish.copy()
        #print(iday, len(fish))
    print('first star area: ', len(fish))


from collections import Counter
ifcc = Counter(initial_fish)


if do_part_two:
    for iday in range(1,256+1):

        next_ifcc = Counter()

        next_ifcc[0] = ifcc[1]
        next_ifcc[1] = ifcc[2]
        next_ifcc[2] = ifcc[3]
        next_ifcc[3] = ifcc[4]
        next_ifcc[4] = ifcc[5]
        next_ifcc[5] = ifcc[6]
        next_ifcc[6] = ifcc[7]
        next_ifcc[7] = ifcc[8]

        next_ifcc[8] = ifcc[0]
        next_ifcc[6] += ifcc[0]

        ifcc = next_ifcc
#        print(iday, ifcc, sum(list(ifcc.values())))

print(iday, ifcc, sum(list(ifcc.values())))
