def equation(x):
    return x**2 - 3*x + 1

def derivative(x):
    return 2*x - 3

def newton_method(initial_guess, tolerance=1e-8, max_iterations=100):         #1e-8 = 1 * 10^-8
    x = initial_guess

    for i in range(max_iterations):
        f_x = equation(x)
        f_prime_x = derivative(x)

        if abs(f_prime_x) < tolerance:
            print("導數靠近0，停止iteration")
            break

        x = x - f_x / f_prime_x

        if abs(f_x) < tolerance:
            print(f"收斂到結果: x = {x} after {i+1} iterations.")
            return x

    print(f"沒有收斂 {max_iterations} iterations.")
    return None

# 設定初始猜測值
initial_guess = 0

newton_solution = newton_method(initial_guess)
