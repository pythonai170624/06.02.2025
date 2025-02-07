

def range_like(from_, to_):
    print(from_)
    if from_ >= to_:
        return
    range_like(from_ + 1, to_)

range_like(1, 10)
print()

# fibb
#             fibb(7) = fibb(6)                           + fibb(5)
#                       fibb(5) + fibb(4)                 + fibb(4) +        fibb(3)
#                       fibb(4)+fibb(3)  fibb(3)+fibb(2)  + fibb(3)+fibb(3)
# 1 1 2 3 5 8 13 21 34
# a b
def fibb(n):
    if n == 1:
        print(1)
        return
    if n == 2:
        print(1, end = " ")
        print(1, end = " ")
        return
    a = 1
    b = 1
    c = 2
    print(a, end=" ")
    print(b, end=" ")
    print(c, end=" ")
    for i in range(n - 3):
        a = b
        b = c
        c = a + b
        print(c, end = " ")
fibb(20)

def fibb_rec(n):
    # 1 2 3 4 5 6 7  8  9
    # 1 1 2 3 5 8 13 21 34
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibb_rec(n-1) + fibb_rec(n-2)
print()
print(fibb_rec(9))