def print_hexagon(rows, cols):
    width = 5  
    height = 3 
    
   
    top_line = "  _  "
    upper_middle_line = " / \\ "
    bottom_line = " \\_/ "

    for row in range(rows):
        for line in range(height):
            for col in range(cols):
                if line == 0:
                    print(top_line, end=" ")
                elif line == 1:
                    print(upper_middle_line, end=" ")
                elif line == 2:
                    print(bottom_line, end=" ")
            print()
        print()

rows = int(input("Enter number of Rows: "))
cols = int(input("Enter number of Columns: "))
print_hexagon(rows, cols)
