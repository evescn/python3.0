def _odd_iter():  # 先构造一个从3开始的奇数序列,偶数必定不是素数
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    # print('x is', x)
    return lambda x: x % n > 0


def primes():
    yield 2  # 输出2这个素数
    it = _odd_iter()
    # list(it)
    while True:
        n = next(it)
        print('primes', n, ' ok')
        yield n
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 20:
        print(n)
    else:
        break
