from Math_pkg.add import add
from Math_pkg.sub import sub
from Math_pkg.mul import mul
from Math_pkg.div import div
from Math_pkg.mod import mod
from Math_pkg.exp import exp
from Math_pkg.sq_root import sq_root

# Perform the operations
result_add = add(1, 2)
result_sub = sub(3, 4)
result_mul = mul(5, 6)
result_div = div(7, 8)
result_mod = mod(9, 10)
result_exp = exp(11, 3)  
result_sq_root = sq_root(25)

print(f"Addition: {result_add}")
print(f"Subtraction: {result_sub}")
print(f"Multiplication: {result_mul}")
print(f"Division: {result_div}")
print(f"Modulus: {result_mod}")
print(f"Power: {result_exp}")
print(f"Square Root: {result_sq_root}")