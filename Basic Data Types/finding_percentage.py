if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    updt = student_marks[query_name]
    sum = float()
    for i in updt:
        sum += i
    print("%.2f" % (sum/3))