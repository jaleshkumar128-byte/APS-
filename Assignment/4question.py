import numpy as np

n = 10000

rolls = np.random.randint(1, 7, size=n)

A = rolls == 1
B = rolls == 6

p_A = np.sum(A) / n
p_B = np.sum(B) / n
p_A_or_B = np.sum(A | B) / n

print("P(A):", p_A)
print("P(B):", p_B)
print("P(A or B):", p_A_or_B)

print("P(A) + P(B):", p_A + p_B)

print("A and B are disjoint:", not np.any(A & B))