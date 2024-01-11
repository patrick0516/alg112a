def equation(x):
    return x**2 - 3*x + 1

def brute_force_method():
    solutions = []
    for x in range(-1000, 1001):  
        if equation(x) == 0:
            solutions.append(x)
    return solutions

brute_force_solutions = brute_force_method()
print("Brute Force Solutions: ", brute_force_solutions)
