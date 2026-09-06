def minion_game(string):
    vowels = "AEIOU"
    
    kevin = 0
    stuart = 0
    
    for i in range(len(string)):
        points = len(string) - i
        
        if string[i] in vowels:
            kevin += points
        else:
            stuart += points
    
    if stuart > kevin:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")
