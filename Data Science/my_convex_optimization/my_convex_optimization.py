import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar, linprog

# Function Definitions
f = lambda x: (x - 1)**4 + x**2
f_prime = lambda x: 4 * (x - 1)**3 + 2 * x

# Plot Function
def print_a_function(f, values):
    plt.plot(values, [f(v) for v in values], label='f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Function Plot')
    plt.grid()
    plt.legend()
    plt.show()

# Bisection Method for Root Finding
def find_root_bisection(f, min_val, max_val, tol=0.001):
    while (max_val - min_val) / 2 > tol:
        midpoint = (min_val + max_val) / 2
        if f(midpoint) == 0:
            return midpoint
        elif f(midpoint) * f(min_val) < 0:
            max_val = midpoint
        else:
            min_val = midpoint
    return (min_val + max_val) / 2

# Newton-Raphson Method for Root Finding
def find_root_newton_raphson(f, f_deriv, x0, tol=0.001, max_iter=100):
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        fpx = f_deriv(x)
        x -= fx / fpx
    return x

# Gradient Descent Method
def gradient_descent(f, f_prime, start, learning_rate=0.1, tol=0.001, max_iter=1000):
    x = start
    for _ in range(max_iter):
        gradient = f_prime(x)
        if abs(gradient) < tol:
            break
        x -= learning_rate * gradient
    return x

# Linear Programming Problem Solver
def solve_linear_problem(A, b, c):
    res = linprog(c, A_ub=A, b_ub=b, method='simplex')
    return res.fun, res.x

# Main Execution
if __name__ == '__main__':
    # Plot the function
    values = np.linspace(-2, 3, 100)
    print_a_function(f, values)

    # Find root using Bisection Method
    root_bisection = find_root_bisection(f_prime, -2, 3)
    print("Root (Bisection):", root_bisection)

    # Find root using Newton-Raphson Method
    root_newton = find_root_newton_raphson(f_prime, lambda x: 12 * (x - 1)**2 + 2, -2)
    print("Root (Newton-Raphson):", root_newton)

    # Find minimum using Gradient Descent
    x_min = gradient_descent(f, f_prime, start=-1, learning_rate=0.01)
    print("Minimum (Gradient Descent):", x_min, f(x_min))

    # Compare with Brent's Method
    res = minimize_scalar(f, method='brent')
    print('Brent Minimum: x = {:.2f}, f(x) = {:.2f}'.format(res.x, res.fun))

    # Solve Linear Programming Problem
    A = np.array([[2, 1], [-4, 5], [1, -2]])
    b = np.array([10, 8, 3])
    c = np.array([-1, -2])
    optimal_value, optimal_arg = solve_linear_problem(A, b, c)
    print("Optimal Value:", optimal_value, "Optimal Arguments:", optimal_arg)
