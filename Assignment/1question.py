import numpy as np

n = 100


tosses = np.random.choice(["Head", "Tail"], size=n)

heads = np.sum(tosses == "Head")
tails = np.sum(tosses == "Tail")

p_head = heads / n
p_tail = tails / n

print("Number of heads:", heads)
print("Number of tails:", tails)
print("Experimental probability of Head:", p_head)
print("Experimental probability of Tail:", p_tail)