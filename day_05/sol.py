import numpy as np

with open('input.txt', 'r') as fp:
    lines = [line.strip() for line in fp.readlines()]


def lines_to_coords(lines):
    coords = []
    for line in lines:
        start, end = line.split(' -> ')
        start = [int(el) for el in start.split(',')]
        end = [int(el) for el in end.split(',')]
        coords.append([start, end])
    return coords

def filter_hv_coords(coords):
    new_coords = []
    for start, end in coords:
        if start[0] == end[0] or start[1] == end[1]:
            new_coords.append([start, end])
    return new_coords

coords = lines_to_coords(lines)
starts = np.array([el[0] for el in coords])
ends = np.array([el[1] for el in coords])


max_val = max(starts.max(), ends.max()) + 1

grid = np.zeros((max_val, max_val))
for start, end in zip(starts, ends):
    if start[0] == end[0]:
        xi = start[0]
        xf = end[0]
        yi, yf = sorted([start[1], end[1]])
    elif start[1] == end[1]:
        xi, xf = sorted([start[0], end[0]])
        yi = start[1]
        yf = end[1]
    else:
        continue

    xf += 1
    yf += 1
    grid[xi:xf, yi:yf] += 1

print('first star answer: ', (grid>=2).sum())


grid = np.zeros((max_val, max_val))
for start, end in zip(starts, ends):
    print(start, end)

    if start[0] == end[0]:
        xi = start[0]
        xf = end[0]
        yi, yf = sorted([start[1], end[1]])
        xf += 1
        yf += 1
        grid[xi:xf, yi:yf] += 1

    elif start[1] == end[1]:
        xi, xf = sorted([start[0], end[0]])
        yi = start[1]
        yf = end[1]
        xf += 1
        yf += 1
        grid[xi:xf, yi:yf] += 1

    else:
        xdiff = np.sign(end[0] - start[0])
        ydiff = np.sign(end[1] - start[1])
        xx = start[0]
        yy = start[1]
        grid[xx,yy] += 1
        print(xx,yy)
        while xx != end[0] + 0:
            xx += xdiff
            yy += ydiff
            grid[xx,yy] += 1
            print(xx,yy)
#        break
print('second star answer: ', (grid>=2).sum())
