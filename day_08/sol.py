import numpy as np

SEGS = [
    'abcefg',  # 0
    'cf',      # 1
    'acdeg',   # 2
    'acdfg',   # 3
    'bcdf',    # 4
    'abdfg',   # 5
    'abdefg',  # 6
    'acf',     # 7
    'abcdefg', # 8
    'abcdfg',  # 9
]


SEGS_MAP = {frozenset(el): ii for ii, el in enumerate(SEGS)}
NUM_SEGS = [len(el) for el in SEGS]
LET_SET = set('abcdefg')

with open('input.txt', 'r') as fp:
    raw_lines = [line.strip() for line in fp.readlines()]

lines = []
for line in raw_lines:
    xin, xout = line.split('|')
    xin = [el for el in xin.split(' ') if el]
    xout = [el for el in xout.split(' ') if el]
    lines.append((xin, xout))


good_sum = 0
good_counts = [NUM_SEGS[ii] for ii in [1,4,7,8]]
for line in lines:
    xout = line[1]
    num_good = sum([len(el) in good_counts for el in xout])
    good_sum += num_good
    print(xout, num_good)
print('good sum: ', good_sum)


xin = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab'.split(' ')
xout = 'cdfeb fcadb cdfeb cdbaf'.split(' ')


def four_digit_from_line(line):
    xin, xout = line

    wire_map = {
        let: set('abcdefg') for let in 'abcdefg'
    }


    for inum in [1, 7, 4, 8]:

        print("inum: ", inum)
        scrambled = set([xx for xx in xin if len(xx)==NUM_SEGS[inum]][0])
        print('scrambled: ', scrambled, 'real: ', SEGS[inum])

        for true_seg in SEGS[inum]:
            wire_map[true_seg] = wire_map[true_seg] & scrambled

        for olet in LET_SET - set(SEGS[inum]):
            for ilet in scrambled:
                if ilet in wire_map[olet]:
                    wire_map[olet].remove(ilet)

        for k,v in wire_map.items():
            print(k, v)
        print()

    # length 5 group
    adg_candidates = set.intersection(*[set(el) for el in xin if len(el)==5])
    for let in 'adg':
        wire_map[let] = wire_map[let] & adg_candidates

    for k, v in wire_map.items():
        if len(v) == 1:
            keep = next(iter(v))
            for kk in LET_SET - set(k):
                if keep in wire_map[kk]:
                    wire_map[kk].remove(keep)

    for k,v in wire_map.items():
        print(k, v)
    print()



    # length 6 group
    abgf_candidates = set.intersection(*[set(el) for el in xin if len(el)==6])
    for let in 'abgf':
        wire_map[let] = wire_map[let] & abgf_candidates

    for k, v in wire_map.items():
        if len(v) == 1:
            keep = next(iter(v))
            for kk in LET_SET - set(k):
                if keep in wire_map[kk]:
                    wire_map[kk].remove(keep)

    for k,v in wire_map.items():
        print(k, v)
    print()


    for k,v in wire_map.items():
        assert(len(v)==1)

    final_wire_map = {next(iter(v)): k  for k,v in wire_map.items()}

    new_segs_map = {}
    for xx in xin:
        new_xx = frozenset(''.join([final_wire_map[el] for el in xx]))
        new_segs_map[frozenset(xx)] = SEGS_MAP[new_xx]

    four_digit = []
    for xx in xout:
        print(xx, new_segs_map[frozenset(xx)])
        four_digit.append(new_segs_map[frozenset(xx)])
    four_digit = int(''.join([str(el) for el in four_digit]))
    return four_digit

all_four_digits = []
for line in lines:
    four_digit = four_digit_from_line(line)
    all_four_digits.append(four_digit)

print("YES!: ", sum(all_four_digits))
sys.exit(1)
