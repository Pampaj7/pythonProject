def fibb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibb(n - 1) + fibb(n - 2)


def fibTab(n):
    table = [0 for i in range(n + 1)]
    table[0] = 0
    table[1] = 1
    table[2] = 1
    for j in range(3, n + 1):
        table[j] = table[j - 1] + table[j - 2]
    return table[n]


def calculateFibonacci(n):
    memoize = [-1 for i in range(n + 1)]
    return calculateFibonacciRec(memoize, n)


def calculateFibonacciRec(memoize, n):
    if n < 2:
        return n
    if memoize[n] >= 0:
        return memoize[n]
    memoize[n] = calculateFibonacciRec(memoize, n - 1) + calculateFibonacciRec(memoize, n - 2)
    return memoize[n]


def fib(n, diz):  # prof metodo top down
    if n == 0 or n == 1:
        return 1
    else:
        if n - 1 in diz:
            a = diz[n - 1]
        else:
            a = fib(n - 1, diz)
        if n - 2 in diz:
            b = diz[n - 2]
        else:
            b = fib(n - 2, diz)
            c = a + b
        diz[n] = c
        return c


def minCoinNum(x): # roba pallosa
    
    MN = [0 for i in range(x + 1)]
    coins = [1, 2, 5, 10, 20, 50, 100, 200, 500]
    for i in range(x+1):
        MN[i] = 123456789
        for j in range(8):  # ?
            if coins[j] <= i and MN[i] > 1 + MN[i - coins[j]]:
                MN[i] = 1 + MN[i - coins[j]]
    return MN[x]


print(fibb(7))
print(calculateFibonacci(8))
print(fibTab(7))
print(minCoinNum(7))
