import time
Order = 3 # The order of the magic square. increase or decrease this value when you want to modify the input. input is: n squared, where n = Order.


# Magic square naive algorithm
def magic_square(n):
    mat = [[0 for _ in range(n)] for _ in range(n)]
    num = 0

    # Check is order is less than 3. if so, return 0 as there are no non-trivial magic squares of an order less than 3
    if n < 3:
        return 0
        # Siamese Method for magic squares of odd order
    elif n % 2 != 0:
        row = 0
        column = n // 2
        cell = 0

        # Assign numbers throughout the matrix via diagonal movement
        for i in range(n * n):
            temp_row = row
            temp_column = column
            cell += 1
            num += 1
            mat[temp_row][temp_column] = num

            # If we've moved n number of times, we need to go down. Otherwise, move diagonally
            if cell == n:
                temp_row += 1
                cell = 0
            else:
                temp_row -= 1
                temp_column += 1

            # If we hit the upper or right edge, we wrap around the matrix accordingly
            if temp_row == -1:
                temp_row = n - 1

            if temp_column == n:
                temp_column = 0


            row = temp_row
            column = temp_column
    # Exchange Method for magic squares of evenly even order
    elif (n//2)%2 == 0:
        offset = n//4 # Order of all partitioned normal squares. Used for moving to different normal squares

        # Fill the Magic Square with consecutive numbers from first element to last element
        for i in range(n):
            for j in range(n):
                num += 1
                mat[i][j] = num


        # Switch the elements in the two top corner odd squares and two top central odd squares with their complementary squares
        for row in range(n//2):
            for column in range(n):
                if row < offset:
                    if (column < offset) or (column > offset*3 - 1):
                        mat[row][column], mat[n - 1 - row][n - 1 - column] = \
                            mat[n - 1 - row][n - 1 - column], mat[row][column]
                else:
                    if (column > offset - 1) and (column < offset*3):
                        mat[row][column], mat[n - 1 - row][n - 1 - column] = \
                            mat[n - 1 - row][n - 1 - column], mat[row][column]
    # Strachey Method for Oddly Even Magic Squares
    elif (n//2)%2 != 0:
        switch = 1 # Switch between the partitioned odd magic squares via "not" keyword
        offset = n//2 # Order of all the partitioned odd magic squares. Used for moving to different odd ordered magic squares
        begColumn = offset//2 # Used to pinpoint the beginning column of ith magic square

        # Create 4 odd magic squares inside the oddly even magic square using the siamese method
        for i in range(4):
            switch = int(not switch) # Used to switch between the beginning rows of the 4 squares
            begRow = offset * switch # beginning row ith square
            cell = 0 # Used to record the number of cells we moved

            if i < 2:
                begColumn = begColumn + begRow
            else:
                begColumn = begColumn - begRow

            row = begRow
            column = begColumn

            # Begin creating the ith square using the siamese method
            for j in range(offset * offset):
                temp_row = row
                temp_column = column
                cell += 1
                num += 1
                mat[temp_row][temp_column] = num

                if cell == offset:
                    temp_row += 1
                    cell = 0
                else:
                    temp_row -= 1
                    temp_column += 1

                if temp_row == begRow - 1:
                    temp_row = begRow - 1 + offset
                if temp_column == offset//2 + begColumn + 1:  #
                    temp_column = offset//2 + begColumn + 1 - offset

                row = temp_row
                column = temp_column

        # Swap the appropriate cells
        for i in range(offset):
            for j in range(n):
                if j < offset // 2 or j > n - offset // 2:
                    if i == offset // 2 and j < offset // 2:
                        mat[i][j + 1], mat[i + offset][j + 1] = mat[i + offset][j + 1], mat[i][j + 1]
                    else:
                        mat[i][j], mat[i + offset][j] = mat[i + offset][j], mat[i][j]

    # Return magic square
    return mat



# Display matrix
def display(matrix):
    for row in range(Order):
        for column in range(Order):
            print(matrix[row][column], end="\t")
        print()


# Test if matrix is a valid magic square
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
    start_time = time.perf_counter() # Starting time
    magic_square(Order) # Run algorithm
    end_time = time.perf_counter() # Ending time

    elapsed_time = end_time - start_time # Evaluate the time it took to create the magic square
    print("Elapsed time:", elapsed_time) # Display the time it to create the magic square

    # Display magic square
    display(magic_square(Order))

    # Test validity of the magic square
    test(magic_square(Order))