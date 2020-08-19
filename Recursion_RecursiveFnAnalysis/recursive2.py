# tail recursion
def calc(n):
    if n > 0:
        k = n ** 2
        print(k)
        calc(n - 1)


# head recursion
def calc_head(n):
    if n > 0:
        calc_head(n - 1)
        k = n ** 2
        print(k)

# tree recursion
def calc_tree(n):
    if n > 0:
        calc_tree(n - 1)
        k = n ** 2
        print(k)
        calc_tree(n - 1)

def calc_indA(n):
    if n > 0:
        k = n ** 2
        print(k)
        calc_indB(n - 1)

def calc_indB(n):
    if n > 0:
        k = n ** 2
        print(k)
        calc_indA(n - 1)

# calc(4)
# calc_head(4)
# calc_tree(3)
calc_indA(4)
