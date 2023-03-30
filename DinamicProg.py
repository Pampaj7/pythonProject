def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


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


print(fib(7))
print(calculateFibonacci(8))
