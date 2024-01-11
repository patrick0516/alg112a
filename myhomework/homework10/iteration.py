def solve_polynomial_bisection(coefficients, lower_bound, upper_bound, epsilon=1e-6, max_iterations=1000):
    lower = lower_bound
    upper = upper_bound

    if evaluate_polynomial(coefficients, lower) * evaluate_polynomial(coefficients, upper) > 0:
        print("初始邊界未包含根。")
        return None

    for _ in range(max_iterations):
        midpoint = (lower + upper) / 2
        fx_mid = evaluate_polynomial(coefficients, midpoint)

        if abs(fx_mid) < epsilon:
            return midpoint

        if fx_mid * evaluate_polynomial(coefficients, lower) < 0:
            upper = midpoint
        else:
            lower = midpoint

    print("未找到解，已達最大選代次數。")
    return None

# ex1：x^5 + 1 = 0
coefficients1 = [1, 0, 0, 0, 0, 1]
root1 = solve_polynomial_bisection(coefficients1, -10, 10)
print("多項式的根:", root1)

# ex2：x^8 + 3x^2 + 1 = 0
coefficients2 = [1, 0, 3, 0, 0, 0, 0, 0, 1]
root2 = solve_polynomial_bisection(coefficients2, -10, 10)
print("多項式的根:", root2)
