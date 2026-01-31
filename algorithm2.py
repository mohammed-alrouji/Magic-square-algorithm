import time
Order = 3 # The order of the magic square. increase or decrease this value when you want to modify the input. input is: n squared, where n = Order.


# Magic square optimized algorithm
def magic_square(n):
    mat = [[0 for _ in range(n)] for _ in range(n)]

    # Check is order is less than 3. if so, return 0 as there are no non-trivial magic squares of an order less than 3
    if n < 3:
        return 0
    # Siamese Method for magic squares of odd order
    elif n%2 != 0:
        num = 0
        row = 0
        column = n//2
        cell = 0

        # Assign numbers throughout the matrix via diagonal movement
        for i in range(n*n):
            cell += 1
            num += 1
            mat[row][column] = num

            # If we've moved n number of times, we need to go down. Otherwise, move diagonally
            if cell == n:
                row += 1
                cell = 0
            else:
                row -= 1
                column += 1

            # If we hit the upper or right edge, we wrap around the matrix accordingly
            if row == -1:
                row = n - 1
            elif column == n:
                column = 0
    # Exchange Method for magic squares of evenly even order
    elif n%4 == 0:
        num = 0
        half = n//2
        fourth = n//4

        # Fill each cell a number according to its coordinates within the matrix
        for i in range(n):
            for j in range(n):
                num += 1

                if i < half:
                    if i < fourth and (j < fourth or j >= fourth * 3):
                        mat[i][j] = (n * n + 1) - num
                    elif i >= fourth and (fourth <= j < fourth * 3):
                        mat[i][j] = (n * n + 1) - num
                    else:
                        mat[i][j] = num
                else:
                    if i >= fourth * 3 and (j < fourth or j >= fourth * 3):
                        mat[i][j] = (n * n + 1) - num
                    elif i < fourth * 3 and (fourth <= j < fourth * 3):
                        mat[i][j] = (n * n + 1) - num
                    else:
                        mat[i][j] = num
    # Strachey Method for Oddly Even Magic Squares
    else:
        num = 0
        switch = 1 # Switch between the partitioned odd magic squares via "not" keyword
        half = n//2 # Order of all the partitioned odd magic squares. Used for moving to different odd ordered magic squares
        fourth = n//4
        begColumn = fourth # Used to pinpoint the beginning column of ith magic square

        # Create 4 odd magic squares inside the oddly even magic square using the siamese method
        for i in range(4):
            switch = int(not switch) # Used to switch between the beginning rows of the 4 squares
            begRow = half * switch # beginning row ith square
            cell = 0 # Used to record the number of cells we moved

            if i < 2:
                begColumn = begColumn + begRow
            else:
                begColumn = begColumn - begRow

            row = begRow
            column = begColumn

            # Begin creating the ith square using the siamese method
            for j in range(half * half):
                cell += 1
                num += 1
                mat[row][column] = num

                if cell == half: # n//2
                    row += 1
                    cell = 0
                else:
                    row -= 1
                    column += 1

                if row == begRow - 1:
                    row = begRow - 1 + half
                elif column == fourth + begColumn + 1: #n//4
                    column = fourth + begColumn + 1 - half

        # Swap the half/2 leftmost columns of the magic squares 1 and 4
        for i in range(half):
            for j in range(fourth):
                mat[i][j], mat[i+half][j] = mat[i+half][j], mat[i][j]

        # Swap back leftmost center element of lesser magic squares 1 and 4
        mat[fourth][0], mat[fourth + half][0] = \
            mat[fourth + half][0], mat[fourth][0]

        # Swap center element of magic squares 1 and 4
        mat[fourth][fourth], mat[fourth + half][fourth] = \
            mat[fourth + half][fourth], mat[fourth][fourth]

        # Swap the rightmost columns of magic squares 2 and 3 two columns after their center column
        for i in range(half):
            for j in range(fourth + half + 2, n):
                mat[i][j], mat[i+half][j] = \
                    mat[i+half][j], mat[i][j]

    # Return magic square
    return mat


# Display the square matrix
def display(matrix):
    for row in range(Order):
        for column in range(Order):
            print(matrix[row][column], end="\t")
        print()


# Test if the square matrix is a valid magic square
def test(matrix):
    magicConstant = Order*(Order*Order + 1)//2

    # Test no duplicates and elements 1...Order*Order are present
    flat = [element for row in matrix for element in row]
    if set(flat) != set(range(1, Order*Order + 1)):
        print("invalid")
        return

    # Test rows
    for row in range(Order):
        if sum(matrix[row]) != magicConstant:
            print("Invalid")
            return

    # Test columns
    for column in range(Order):
        if sum(matrix[row][column] for row in range(Order)) != magicConstant:
            print("Invalid")
            return

    # Test first diagonal
    if  sum(matrix[i][i] for i in range(Order))!= magicConstant:
        print("Invalid")
        return

    # Test second diagonal
    if sum(matrix[i][Order-1-i] for i in range(Order))!= magicConstant:
        print("Invalid")
        return

    print("Valid")
    return


# Main program block
if __name__ == "__main__":
    # Test the timing of the creation of the magic square
    start_time = time.perf_counter()  # Starting time
    magic_square(Order)  # Run algorithm
    end_time = time.perf_counter()  # Ending time

    elapsed_time = end_time - start_time  # Evaluate the time it took to create the magic square
    print("Elapsed time:", elapsed_time)  # Display the time it to create the magic square

    # Display magic square
    display(magic_square(Order))

    # Test validity of the magic square
    test(magic_square(Order))