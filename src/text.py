from collections import defaultdict
import math

# Provided permutations
permutations = [
    [1, 3, 7, 4, 8, 6, 5, 2],
    [3, 5, 6, 4, 8, 1, 7, 2],
    [1, 4, 5, 2, 8, 3, 7, 6],
    [6, 3, 7, 1, 5, 8, 4, 2],
    [1, 3, 6, 5, 2, 4, 8, 7],
    [3, 1, 4, 7, 5, 8, 6, 2],
    [1, 4, 7, 2, 6, 8, 5, 3],
    [5, 1, 4, 6, 7, 2, 8, 3],
    [1, 8, 6, 2, 3, 5, 7, 4],
    [1, 5, 7, 4, 6, 3, 8, 2],
    [1, 5, 6, 7, 2, 4, 8, 3],
    [1, 2, 3, 8, 6, 7, 5, 4],
    [1, 2, 7, 5, 8, 3, 6, 4],
    [3, 6, 1, 8, 4, 7, 2, 5],
    [3, 5, 2, 6, 8, 1, 7, 4],
    [6, 2, 4, 5, 1, 3, 8, 7],
    [1, 4, 6, 3, 8, 5, 7, 2],
    [3, 2, 1, 6, 8, 5, 4, 7],
    [1, 6, 5, 8, 4, 7, 3, 2],
    [5, 1, 8, 3, 7, 2, 6, 4]
]

# Initialize dictionaries to store the points for each number for each case
points_case_1 = defaultdict(int)
points_case_2 = defaultdict(int)
points_case_3 = defaultdict(int)
points_case_4 = defaultdict(int)

# Scoring schemes
linear_scheme = [8, 7, 6, 5, 4, 3, 2, 1]
gap_scheme = [11, 9, 8, 7, 4, 3, 2, 0]

# Calculate points for each case
for perm in permutations:
    for idx, num in enumerate(perm):
        # Case 1: Linear Decrease with Position
        points_case_1[num] += linear_scheme[idx]
        
        # Case 2: Exponential Decrease with Position
        points_case_2[num] += 8 * (0.5 ** idx)
        
        # Case 3: Linear Decrease with Bigger Gap
        points_case_3[num] += gap_scheme[idx]
        
        # Case 4: Custom Scheme (Square Root)
        points_case_4[num] += math.sqrt(9 - (idx + 1))
        
# print(
#     points_case_1,
#     points_case_2,
#     points_case_3,
#     points_case_4
# )

# print()

# Sort the dictionaries by key for easier comparison
points_case_1 = dict(sorted(points_case_1.items()))
points_case_2 = dict(sorted(points_case_2.items()))
points_case_3 = dict(sorted(points_case_3.items()))
points_case_4 = dict(sorted(points_case_4.items()))

print(
    points_case_1, "\n",
    points_case_2, "\n",
    points_case_3, "\n",
    points_case_4,  "\n"
)

print()

points_case_1 = dict(sorted(points_case_1.items(), key=lambda x: x[1], reverse=True))
points_case_2 = dict(sorted(points_case_2.items(), key=lambda x: x[1], reverse=True))
points_case_3 = dict(sorted(points_case_3.items(), key=lambda x: x[1], reverse=True))
points_case_4 = dict(sorted(points_case_4.items(), key=lambda x: x[1], reverse=True))

print(
    points_case_1, "\n",
    points_case_2, "\n",
    points_case_3, "\n",
    points_case_4,  "\n"
)

print()

print(
    list(points_case_1.keys()), "\n",
    list(points_case_2.keys()), "\n",
    list(points_case_3.keys()), "\n",
    list(points_case_4.keys()),  "\n"
)