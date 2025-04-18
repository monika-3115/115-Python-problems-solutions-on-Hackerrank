if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        op = input().split()
        match op[0]:
            case 'insert':
                l.insert(*map(int, op[1:]))
            case 'print':
                print(l)
            case 'remove':
                l.remove(int(op[1]))
            case 'append':
                l.append(int(op[1]))
            case 'sort':
                l.sort()
            case 'pop':
                l.pop()
            case 'reverse':
                l.reverse()