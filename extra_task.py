#Akmurzayev Zhanarys
#Calculus 2
#Библиотеки который нужно установить:
# "pip install numpy matplotlib sympy" нужно ввести в командную строку


import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def get_user_function():
    expression_str = input("Please, type the function f(x): ")
    x = sp.symbols('x')
    try:
        expression = sp.sympify(expression_str)
        f = sp.lambdify(x, expression, 'numpy')
        return f
    except sp.SympifyError:
        print("Function Entry Error.")
        return get_user_function()

def get_user_input():
    a_str = input("Please, enter the value of a: ")
    b_str = input("Please, enter the value of b: ")
    n = int(input("Please, enter the number of partitions n: "))
    return a_str, b_str, n

def trapezoidal_rule(a, b, n, f):
    x = np.linspace(float(a), float(b), n+1)
    h = (float(b) - float(a)) / n
    integral = h * (f(float(a)) + 2 * sum(f(x[i]) for i in range(1, n)) + f(float(b))) / 2
    return integral

def simpsons_rule(a, b, n, f):
    x = np.linspace(float(a), float(b), n+1)
    h = (float(b) - float(a)) / n
    integral = h/3 * (f(float(a)) + 4*sum(f(x[i]) for i in range(1, n, 2)) +
                     2*sum(f(x[i]) for i in range(2, n-1, 2)) + f(float(b)))
    return integral

def plot_function_and_integral(a_str, b_str, n, f):
    a = sp.sympify(a_str)
    b = sp.sympify(b_str)

    x_vals = np.linspace(float(a), float(b), 1000)
    y_vals = f(x_vals)

    plt.plot(x_vals, y_vals, label='f(x)')
    plt.fill_between(x_vals, y_vals, alpha=0.2, label='Area under the curve')

    trapezoidal_integral = trapezoidal_rule(a, b, n, f)
    simpsons_integral = simpsons_rule(a, b, n, f)

    print(f'Trapezoidal Rule: {trapezoidal_integral}')
    print(f'Simpson\'s Rule: {simpsons_integral}')

    plt.title('GRAPHIC WICH CREATE ZHANARYS :)')
    plt.legend()
    plt.show()

user_function = get_user_function()
a, b, n = get_user_input()
plot_function_and_integral(a, b, n, user_function)
