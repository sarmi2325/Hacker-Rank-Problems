    n = int(input())
     student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    s=(sum(student_marks[query_name]))
    c=len(student_marks[query_name])
    f=s/c
    print(f"{f:.2f}")

