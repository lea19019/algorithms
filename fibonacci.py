def fibonacci(num):
    memo = {}
    def fib(n):
        if n <= 1:
            return n
        if n in memo:
            return memo[n]

        res = fib(n - 1) + fib(n - 2)
        memo[n] = res
        return res
    val = fib(num)
    # print('num', num)
    # print(memo)
    return val


if __name__ == '__main__':
    res1 = fibonacci(1)
    res3 = fibonacci(3)
    res5 = fibonacci(5)
    res7 = fibonacci(7)
    res10 = fibonacci(10)
    res30 = fibonacci(30)
    res100 = fibonacci(100)
    res998 = fibonacci(998)
    print('res1', res1)
    print('res3', res3)
    print('res5', res5)
    print('res7', res7)
    print('res10', res10)
    print('res30', res30)
    print('res100', res100)
    print('res998', res998)
    print('res998 len', len(str(res998)))
    