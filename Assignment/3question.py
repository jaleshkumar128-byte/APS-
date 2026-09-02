import numpy as np

n = 6000

rolls = np.random.randint(1, 7, size=n)

for outcome in range(1, 7):
    count = np.sum(rolls == outcome)
    probability = count / n

    print("Outcome:", outcome)
    print("Count:", count)
    print("Experimental probability:", probability)
    print()