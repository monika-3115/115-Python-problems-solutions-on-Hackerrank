if __name__ == '__main__':
    dict = {}
    key_names = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dict[name] = score
    unique_sort_score =sorted(set(dict.values()))
    second_grade = unique_sort_score[1]
    for key, value in dict.items():
        if value == second_grade:
            key_names.append(key)
    for i in sorted(key_names):
        print(i)