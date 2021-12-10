from collections import Counter
import numpy as np


with open('input.txt', 'r') as fp:
    raw_lines = [line.strip() for line in fp.readlines()]


lines = []
for line in raw_lines:
    lines.append([int(el) for el in line])
heights = np.array(lines)


def get_lrud(ii, jj, heights):

    # left  ii, jj-1
    # right ii, jj+1
    # up    ii-1, jj
    # down  ii+1, jj

    if jj == 0:
        left = 10
    else:
        left = heights[ii, jj-1]

    if jj == heights.shape[1] - 1:
        right = 10
    else:
        right = heights[ii, jj+1]

    if ii == 0:
        up = 10
    else:
        up = heights[ii-1, jj]

    if ii == heights.shape[0] - 1:
        down = 10
    else:
        down = heights[ii+1, jj]

    return left, right, up, down



low_points = []
low_heights = []
for ii in range(heights.shape[0]):
    for jj in range(heights.shape[1]):
        left, right, up, down = get_lrud(ii, jj, heights)
        height = heights[ii,jj]
        compares = np.array([left, right, up, down])
        if height < compares.min():
            low_points.append((ii,jj))
            low_heights.append(height)

low_heights = np.array(low_heights)
low_points = set(low_points)
print('risk level: ', (low_heights + 1).sum())



basin_paths = {}
for start_ii in range(heights.shape[0]):
    for start_jj in range(heights.shape[1]):

        ii = start_ii
        jj = start_jj
        height = heights[ii,jj]
        if height == 9:
            continue

        path = []
        point = (ii, jj)
#        print('start point: ', point)

        while point not in low_points:

            path.append(point)
            left, right, up, down = get_lrud(ii, jj, heights)
            argmin = np.argmin([left, right, up, down])
            if argmin == 0:
                jj = jj - 1
            elif argmin == 1:
                jj = jj + 1
            elif argmin == 2:
                ii = ii - 1
            elif argmin == 3:
                ii = ii + 1

            point = (ii, jj)
#            print('  point: ', point)

        path.append(point)
        basin_paths[(start_ii, start_jj)] = path


basin_sizes = Counter()
for start_point, path in basin_paths.items():
    end_point = path[-1]
    basin_sizes[end_point] += 1

top3 = basin_sizes.most_common(3)
final_mult = np.product([el[1] for el in top3])
print('final_mult: ', final_mult)
