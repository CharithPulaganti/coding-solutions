

# Complete the solve function below.
def solve(s):
    words = s.split(' ')
    result = []
    
    for word in words:
        if word:
            word = word[0].upper() + word[1:]
        result.append(word)
    
    return ' '.join(result)
