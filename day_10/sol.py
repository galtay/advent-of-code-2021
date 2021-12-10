from collections import Counter

SCORES_1 = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
SCORES_2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


LEFTS = set(['(', '[', '{', '<'])
RIGHTS = set([')', ']', '}', '>'])
COMPLIMENTS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

with open('input.txt', 'r') as fp:
    lines = [line.strip() for line in fp.readlines()]

first_illegal_chars = []
new_lines = []
for line in lines:
    is_corrupt = False
    needs_to_close = []
    for char in line:
        if char in LEFTS:
            needs_to_close.append(char)
        elif char in RIGHTS:
            expected = COMPLIMENTS[needs_to_close[-1]]
            if expected == char:
                needs_to_close.pop()
            else:
#                print(line, 'expected', expected, 'but found', char)
                first_illegal_chars.append(char)
                is_corrupt = True
                break

    if not is_corrupt:
        new_lines.append(line)

score = 0
for char in first_illegal_chars:
    score += SCORES_1[char]
print('score: ', score)


scores = []
for line in new_lines:
    needs_to_close = []
    for char in line:
        if char in LEFTS:
            needs_to_close.append(char)
        elif char in RIGHTS:
            expected = COMPLIMENTS[needs_to_close[-1]]
            if expected == char:
                needs_to_close.pop()
            else:
                print('WOOPS')
                sys.exit(1)

    to_complete = [COMPLIMENTS[el] for el in reversed(needs_to_close)]
    score = 0
    for char in to_complete:
        score = score * 5 + SCORES_2[char]
    scores.append(score)

scores = sorted(scores)
score = scores[len(scores)//2]
print('score: ', score)
