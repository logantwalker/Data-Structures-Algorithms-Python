# writing functions to display square of n numbers. iterative vs. recursive

def calculate_itr(n):
    while n > 0:
        k = n ** 2
        print(k)
        n = n - 1

calculate_itr(4)


def calculate_rec(n):
    if n > 0:
        k = n ** 2
        print(k)
        calculate_rec(n - 1)

calculate_rec(4)

