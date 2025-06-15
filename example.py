import math

# Define the function to integrate
def f(x, y):
    return math.exp(x + y)

# Integration bounds: [0, ln2] x [0, ln3]
a, b = 0, math.log(2)
c, d = 0, math.log(3)

# Calculate the integral
result = double_integral_compound(f, a, b, c, d)
print(f"Approximate double integral: {result:.10f}")
