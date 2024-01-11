# 方法 1
def power2n(n):
    return 2**n

# 方法 2a：用遞迴
def power2n_recursive_a(n):
    if n == 0:
        return 1
    return power2n_recursive_a(n - 1) + power2n_recursive_a(n - 1)

# 方法 2b：用遞迴
def power2n_recursive_b(n):
    if n == 0:
        return 1
    return 2 * power2n_recursive_b(n - 1)

# 方法 3：用遞迴+查表
def power2n_recursive_with_table(n, memo=None):
    if memo is None:
        memo = {}

    if n == 0:
        return 1

    if n not in memo:
        memo[n] = power2n_recursive_with_table(n - 1, memo) + power2n_recursive_with_table(n - 1, memo)

    return memo[n]

# 測試
n = 10
print(f'Method 1: power2n({n}) = {power2n(n)}')
print(f'Method 2a: power2n_recursive_a({n}) = {power2n_recursive_a(n)}')
print(f'Method 2b: power2n_recursive_b({n}) = {power2n_recursive_b(n)}')
print(f'Method 3: power2n_recursive_with_table({n}) = {power2n_recursive_with_table(n)}')
