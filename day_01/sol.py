with open('input.txt', 'r') as fp:
    dat = fp.read()
depths = [int(el) for el in dat.split('\n') if el]


def get_diffs(arr):
    return [second-first for second, first in zip(arr[1:], arr[:-1])]


diffs = get_diffs(depths)
print(sum([el > 0 for el in diffs]))


ii=0
ff=ii+3
trips = []
while ff <= len(depths):
    trips.append(depths[ii:ff])
    ii += 1
    ff += 1

trips_sums = [sum(el) for el in trips]
diffs = get_diffs(trips_sums)
print(sum([el > 0 for el in diffs]))
