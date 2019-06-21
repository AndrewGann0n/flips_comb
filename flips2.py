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

def chance_table(base):
    total = 0.0
    n = 1
    while True:
        total += chance_at(base, n)
        n += 1
        yield total

# print(chance_table(2, 10))
# print(chance_table(3, 10))
# print(chance_table(4, 10))
# print(chance_table(5, 10))


n_items = int(raw_input('Number of items: '))

chance_gen = chance_table(n_items)
chances = []

rounds = 10000
total_iterations = 0

# I don't recommend using this for anything higher than r = 4

'''
Previously, you had the rand declaration within the while loop. However, we should only be declaring it once.
The chance table gives us the chance of finding that combo BY THAT DEPTH. We should not be rerolling at each depth. 
'''
for _ in xrange(rounds):
    it = 0
    # Good lord this balloons, even for r = 4. I had to do this, as a rand of .989 causes a segfault.
    rand = random.uniform(0, .987)
    # print rand
    while True:
        if it >= len(chances):
            a = next(chance_gen)
            chances.append(next(chance_gen))
        if rand < chances[it]:
            total_iterations += it + 1
            break
        it += 1

print chances
print(total_iterations * 1.0 / rounds)
