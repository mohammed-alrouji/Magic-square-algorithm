MAGIC SQUARE ALGORITHM TUTORIAL

LIBRARIES:
We import "time" to test how fast our algorithm is.

HOW TO CHANGE INPUT (order of the magic square):
the second line which reads "Order = 3" is the order of the magic square you want to create, which is the input for our algorithm. simply change the number and run the program to get a magic square of that order.

WARNING: You must keep in mind that the input you enter will be squared in the algorithm, because it is the order of the square matrix that will be created. so when you enter the input 55 for example, it will create a square matrix filled with 3025 elements! We have faced technical problems when the input was near or beyond 10000.

FUNCTIONS:
1- magic_square(n): this is our project's magic square algorithm itself, which implements three other lesser algorithms.

2- display(matrix): this will display the magic square that's been created.

3- test(matrix): this will test if the magic square created of the current order is a valid non-trivial magic square or not.

MAIN BLOCK:
In the main block you will find function calls to all previuosly mentioned functions. simply comment them out if you dont want to see their outputs. you will also see the timing functions used to test the time of the algorithm. you can also comment out the print statment if you dont wish to see the timing.


