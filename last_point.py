import numpy as np

def double_integral_compound(f, a, b, c, d, nx=100, ny=100):
    """
    Approximates the double integral of f(x, y) over [a,b] × [c,d] 
    using the composite trapezoidal rule.
    
    Parameters:
        f  : function of two variables f(x, y)
        a, b : float, bounds for x
        c, d : float, bounds for y
        nx : int, number of subintervals in x
        ny : int, number of subintervals in y
        
    Returns:
        float, approximate value of the integral
    """
    x = np.linspace(a, b, nx + 1)
    y = np.linspace(c, d, ny + 1)
    hx = (b - a) / nx
    hy = (d - c) / ny
    
    integral = 0.0
    for i in range(nx + 1):
        for j in range(ny + 1):
            weight = 1
            if i == 0 or i == nx:
                weight *= 0.5
            if j == 0 or j == ny:
                weight *= 0.5
            integral += weight * f(x[i], y[j])
    
    return integral * hx * hy
