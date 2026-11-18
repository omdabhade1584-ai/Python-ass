# Pattern 1
n = 7

for i in range(n):
    for j in range(n):
        if i == n // 2 or j == n // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    print()

# --------------------------------------------------------------------------------------------------------------
# Pattern 2
n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    print()

# -----------------------------------------------------------------------------------------------------------------
# Problem 3
n = 4

# Upper half
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")

    print("*", end=" ")

    if i > 0:
        for j in range(2 * i - 1):
            print(" ", end=" ")
        print("*", end=" ")

    print()

# Lower half
for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(" ", end=" ")

    print("*", end=" ")

    if i > 0:
        for j in range(2 * i - 1):
            print(" ", end=" ")
        print("*", end=" ")

    print()
    # -------------------------------------------------------------------------------------------------------------
    # Problem 4