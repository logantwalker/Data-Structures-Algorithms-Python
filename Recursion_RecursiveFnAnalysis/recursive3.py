# Sum of N numbers: recursive solution
# sum(n) = sum(n-1) + n for n>1
# sum(n) = 1 for n = 1
def sum(n):
    if n == 0:
        return 0
    return sum(n-1) + n

print(sum(5))

# time complexity
# O(n+1)