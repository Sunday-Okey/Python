# Math Module Part I
import math
import random
import statistics
import itertools

# Constants
# print(math.pi)
# print(math.e)
# print(math.nan)
# print(math.inf)
# # Trigonometry

# # Ceiling and Floor
# cookies = 10.3
# candy = 7
# print(math.ceil(cookies))
# print(math.ceil(candy))

# age = 47.9
# otherage = 47

# print(math.floor(age))
# print(math.floor(otherage))
# print(math.factorial(5))
# print(math.sqrt(64))

# print(math.gcd(52, 8))

# print(random.random())
# decider = random.randrange(2)
# if decider == 0:
#     print("HEADS")
# else:
#     print("TAILS")
    
# print(random.randrange(1, 7))

# lotterywinners = random.sample(range(100), 5)
# print(lotterywinners)
# possiblepets = ["cat", "dog", "fish"]
# print(random.choice(possiblepets))

# cards = ["Jack", "Queen", "Kind", "Ace"]
# random.shuffle(cards)
# print(cards)

# agesdata = [10, 13, 14, 12, 11, 10, 11, 10, 15]
# print(statistics.mean(agesdata))
# print(statistics.mode(agesdata))
# print(statistics.median(agesdata))

# print(statistics.variance(agesdata))
# print(statistics.stdev(agesdata))

# for x in itertools.count(50, 5):
#     print(x)
#     if x == 60:
#         break
# x = 0
# for c in itertools.cycle([1, 2, 3, 4]):
#     print(c)
#     x += 1
#     if x > 50:
#         break

for r in itertools.repeat(4):
    print(r)

election = {1: "Barb", 2: "Karen", 3:"Erin"}

# for p in itertools.permutations(election.values()):
#     print(p)

# for p in itertools.combinations(election.values(), 2):
#     print(p)
# math.hypot()