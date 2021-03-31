n = int(input())
r = 1
if n == 1:
    print(r)
else:
    n-=1
    while True:
        if n-6*r <= 0:
            print(r+1)
            break
        else:
            n -= 6*r
            r += 1

