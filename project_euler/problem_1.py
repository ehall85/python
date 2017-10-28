#
# Solution to Project Euler Problem 1

def sum():
    total = 0
    for x in range(0, 1000):
        if (x % 3 == 0 or x % 5 == 0):
            total = total + x
    print(total)

if __name__ == "__main__":
    sum()
