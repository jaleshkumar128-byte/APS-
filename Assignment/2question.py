import numpy as np

for n in [10, 100, 1000, 10000]:
    tosses = np.random.choice(["Head", "Tail"], size=n)

    heads = np.sum(tosses == "Head")
    p_head = heads / n

    print("Number of trials:", n)
    print("Heads:", heads)
    print("Experimental probability of Head:", p_head)
    print()