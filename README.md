# Jacobi-and-Gauss-seidel-method
this repository will demonstrate how to apply Jacobi and Gauss seidel's methods to calculate with the desired accuracy, the self-values and self-vectors of the matrix A


# Jacobi method - quick review:
In numerical analysis, Jacobian iterations for finding self-values, is an iterative method that gives, with the desired accuracy, the self-values and self-vectors of matrix A, when A is hermetic (or symmetric). The method is named after the mathematician Yaakov Yaakobi. The idea of the method is to attach in each iteration the matrix in a unitary matrix so that the sum of the quadrilateral limbs outside the diagonal is reduced, thus slanting the matrix.

# Gauss-seidel method - quick review:
this method is an iterative method for solving a system of linear equations, And very similar to the Jacobi method, Although it can be applied to any matrix with non-zero members on the main diagonal, its convergence is only guaranteed if the matrix is dominant diagonally, or is symmetrical and positive.
The advantage of this method over the elimination method is the advantage of all iterative methods - these methods take advantage of the thinness of matrices more efficiently, and in cases of particularly sparse matrices save a lot of time while running



# How it works? 

* algorithem's steps:

1. insert a matrix in a form of a list: </br>
``` bash
matX = [[1,2,3],[4,5,6],[7,8,9]]
```
2. the algorithem will check if there is a Dominant diagonal in the inserted matrix, if not, it will try to swap the rows/colums to find the right diagonal.
3. if the conditions are matched, we will apply the following equations: </br>

# Jacobi method: <br/>
![Jacobi method](https://i.ibb.co/NLkRfkP/image.jpg)

# Gauss-seidel method: <br/>
![Gauss-seidel method](https://i.ibb.co/6tMHJWy/image.jpg)

we will stop after Xr+1 - Xr < epsilon.</br></br>
4. the results (Xr+1,Yr+1,Zr+1...etc) will be printed.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install sympy and Texttable.

```bash
pip install numpy
```

```bash
pip install Texttable
```


## Contributing
I built the algorithm in the form of object-oriented programming, in order to simplify the idea behind it. <br/>
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

