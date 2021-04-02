import sys
num = int(input())

for i in range(num):  # num 수 만큼 반복
    a = list(sys.stdin.readline())  #OX 받음
    c = 1
    res = 0

    for i in a:
        if i == 'O':
            res += c
            c += 1
        else:
            c = 1
    print(res)






