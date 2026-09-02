import numpy as np

n = 10000

coin = np.random.choice(["Head", "Tail"], size=n)
die = np.random.randint(1, 7, size=n)

A = coin == "Head"
B = die % 2 == 0

p_A = np.sum(A) / n
p_B = np.sum(B) / n
p_A_and_B = np.sum(A & B) / n

print("P(A):", p_A)
print("P(B):", p_B)
print("P(A and B):", p_A_and_B)

print("P(A) * P(B):", p_A * p_B)