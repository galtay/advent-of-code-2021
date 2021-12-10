import numpy as np

with open('input.txt', 'r') as fp:
    lines = fp.readlines()
lines = [
    [int(el) for el in list(line.strip())] for line in lines
]

nums = np.array(lines)
colsums = nums.sum(axis=0)

gamma_bits_int = (colsums >= nums.shape[0]//2).astype(int)
gamma_bits_str = [str(el) for el in gamma_bits_int]
gamma = int(''.join(gamma_bits_str), 2)

epsilon_bits_int =  (colsums < nums.shape[0]//2).astype(int)
epsilon_bits_str = [str(el) for el in epsilon_bits_int]
epsilon = int(''.join(epsilon_bits_str), 2)

print('gamma: ', gamma)
print('epsilon: ', epsilon)
print('gamma * epsilon: ', gamma * epsilon)
print()



nn = nums.copy()
for ii in range(nn.shape[1]):
    print('bit position: ', ii)
    count_0 = (nn[:,ii] == 0).sum()
    count_1 = (nn[:,ii] == 1).sum()
    if count_1 >= count_0:
        most_common = 1
    else:
        most_common = 0

    print('count_0: ', count_0, 'count_1: ', count_1, 'most_common: ', most_common)
    mask = nn[:,ii] == most_common
    nn = nn[mask]
    if nn.shape[0] == 1:
        nn = nn.flatten()
        nn_str = [str(el) for el in nn]
        oxygen = int(''.join(nn_str), 2)
        print('oxygen: ', oxygen)
        break



nn = nums.copy()
for ii in range(nn.shape[1]):
    print('bit position: ', ii)
    count_0 = (nn[:,ii] == 0).sum()
    count_1 = (nn[:,ii] == 1).sum()
    if count_0 <= count_1:
        least_common = 0
    else:
        least_common = 1

    print('count_0: ', count_0, 'count_1: ', count_1, 'least_common: ', least_common)
    mask = nn[:,ii] == least_common
    nn = nn[mask]
    if nn.shape[0] == 1:
        nn = nn.flatten()
        nn_str = [str(el) for el in nn]
        c02 = int(''.join(nn_str), 2)
        print('c02: ', c02)
        break

print('oxygen * c02: ', oxygen * c02)
