import random

n_items = int(raw_input('Number of items: '))

rounds = 10000
total_iterations = 0.0

for _ in xrange(rounds):
    items = set(xrange(n_items))
    while len(items) > 0:
        total_iterations += 1
        chosen = random.randint(0, n_items - 1)
        if chosen in items:
            items.remove(chosen)

print(total_iterations/rounds)
