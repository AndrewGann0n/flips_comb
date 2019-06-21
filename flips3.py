import random
import itertools
import math

def comb_mult(base, draws):
    if draws == 0:
        return 1.0
    comb_sum = 0.0
    combs = list(itertools.product(range(1, base), repeat=draws))
    for i in xrange(len(combs)):
        comb = list(combs[i])
        comb.sort()
        comb = map(lambda x: str(x), comb)
        comb = ','.join(comb)
        combs[i] = comb
    combs = list(set(combs))
    for i in xrange(len(combs)):
        comb = combs[i].split(',')
        comb = map(lambda x: int(x), comb)
        combs[i] = comb
    for comb in combs:
        comb_sum += reduce((lambda x, y: x * y), comb)
    return comb_sum

def chance_at(base, depth):
    if depth < base:
        return 0.0
    return math.factorial(base-1)*comb_mult(base, depth - base)/math.pow(base, depth-1)

n_items = int(raw_input('Number of items: '))

min_chance = 0.001
avg = 0.0
total_chance = 0.0
n = n_items

while True:
    chance = chance_at(n_items, n)
    print chance
    avg += chance * n
    total_chance += chance
    if chance < min_chance:
        break
    n += 1

print n
print avg / total_chance
