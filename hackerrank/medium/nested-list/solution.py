if __name__ == '__main__':
    n = int(input())
    students = []
    for _ in range(n):
        name = input()
        grade = float(input())
        students.append([name, grade])
    grades =[]
        
    for student in students:
        grades.append(student[1])
    
    grades = list(set(grades))
    grades.sort()
        
    second_lowest = grades[1]
        
    names = []
        
    for student in students:
        if student[1] == second_lowest:
            names.append(student[0])
    names.sort()
    for name in names:
        print(name)
