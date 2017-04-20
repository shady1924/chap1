import random

trials = 1000000
hits = 0

for i in range(trials):
    x = random.random()
    y = random.random()
    
    if x * x + y * y <= 1:
        hits += 1
pi = 4 * hits / trials
print(pi) 
