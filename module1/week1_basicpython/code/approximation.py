def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
def approximate_sin(x, n):
    assert n > 0, 'n must be greater than zero'
    approx = 0
    for i in range(n):
        approx += ((-1) ** i) * (x ** (2 * i + 1) / factorial(2 * i + 1))
    return approx
def approximate_cos(x, n):
    assert n > 0
    approx = 0
    for i in range(n):
        approx += ((-1) ** i) * (x ** (2 * i) / factorial(2 * i))
    return approx
def approximate_sinh(x, n):
    assert n > 0
    approx = 0
    for i in range(n):
        approx += x ** (2 * i + 1) / factorial(2 * i + 1)
    return approx
def approximate_cosh(x, n):
    assert n > 0
    approx = 0
    for i in range(n):
        approx += x ** (2 * i) / factorial(2 * i)
    return approx
