import sympy as sp

x = sp.symbols('x')

def hermite_interpolation(points, values, derivatives):
    n = len(points)
    H = 0
    for i in range(n):

        Li = 1
        for j in range(n):
            if i != j:
                Li *= (x - points[j]) / (points[i] - points[j])

        L_prime = sp.diff(Li, x)
        Hi = (1 - 2 * (x - points[i]) * L_prime.subs(x, points[i])) * Li**2 * values[i]
        if derivatives[i] is not None:
            Hi += (x - points[i]) * Li**2 * derivatives[i]
        
        H += Hi
    
    return sp.simplify(H)

points_1 = [1, 2, 3]
values_1 = [0, 0, 1]
derivatives_1 = [0, 0, None]

hermite_poly_1 = hermite_interpolation(points_1, values_1, derivatives_1)
print("the polynomial of question1: ")
sp.pretty_print(hermite_poly_1)

points_2 = [0, 1, 2]
values_2 = [0, 1, 1]
derivatives_2 = [0, 1, None]

hermite_poly_2 = hermite_interpolation(points_2, values_2, derivatives_2)
print("the polynomial of question2: ")
sp.pretty_print(hermite_poly_2)
