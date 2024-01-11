from datetime import datetime

# 原始遞迴版本
fib = [None] * 10000
fib[0] = 0
fib[1] = 1

def fibonacci_recursive(n):
    if n < 0: raise ValueError("Input must be a non-negative integer.")
    if not fib[n] is None: return fib[n]
    fib[n] = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    return fib[n]

# n = 35
n = 60
startTime = datetime.now()
print(f'fibonacci_recursive({n}) = {fibonacci_recursive(n)}')
endTime = datetime.now()
seconds = endTime - startTime
print(f'Time: {seconds}')

# 改寫為迴圈版本
def fibonacci_iterative(n):
    fib = [None] * (n + 1)
    fib[0], fib[1] = 0, 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

# n = 35
# n = 60
n = 10000 

startTime = datetime.now()
result = fibonacci_iterative(n)
endTime = datetime.now()

print(f'fibonacci_iterative({n}) = {result}')
print(f'Time: {endTime - startTime}')

