import numpy as np

with open('input.txt', 'r') as fp:
    lines = [line.strip() for line in fp.readlines()]

pos = np.array([int(el) for el in lines[0].split(',')])

costs = []
for trial in range(min(pos), max(pos) + 1):
    cost = np.abs(pos - trial).sum()
    costs.append(cost)
costs = np.array(costs)

ii = np.argmin(costs)
print('best pos: ', ii)
print('best cost: ', costs[ii])


costs = []
for trial in range(min(pos), max(pos) + 1):
    diffs = np.abs(pos - trial)
    costs_1 = diffs * (diffs + 1) / 2
    cost = costs_1.sum()
    costs.append(cost)
costs = np.array(costs)

ii = np.argmin(costs)
print('best pos: ', ii)
print('best cost: ', costs[ii])
