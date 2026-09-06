def print_rangoli(size):
    import string
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    width = 4 * size -3
    
    for i in range(size):
        row = ""
        
        for j in range(i + 1):
            if j > 0:
                row +="-"
            row += alphabet[size -1 -j]
        
        for j in range(i -1, -1, -1):
            row += "-"
            row += alphabet[size - 1 -j]
        print(row.center(width, "-"))
    
    for i in range(size - 2, -1, -1):
        row = ""
        
        for j in range(i + 1):
            if j > 0:
                row += "-"
            row += alphabet[size - 1 -j]
        for j in range(i - 1, -1, -1):
            row += "-"
            row += alphabet[size -1 -j]
        print(row.center(width, "-"))
