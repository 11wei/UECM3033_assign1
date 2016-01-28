import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( sy.sin(x)/x), ((x,0, sy.oo))
    return ans

def my_solution():
    A = np.array( [[1,4,6,3,6,8,2,4,7,5],
                   [3,2,4,5,6,7,5,3,1,3],
                   [2,3,5,6,7,5,3,2,4,5],
                   [3,6,7,5,3,1,3,4,5,7],
                   [4,5,6,4,3,2,4,5,6,7],
                   [6,8,6,3,4,6,7,5,4,5],
                   [3,4,6,4,3,2,3,5,6,7],
                   [4,5,3,2,4,5,3,2,4,5],
                   [5,3,3,5,6,8,6,4,3,2],
                   [3,4,6,7,6,4,3,2,3,4]])
    b = np.array([1,2,7,6,5,4,3,2,1,5])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1304414
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
