import sys

a,b,c = map(float, sys.stdin.readline().split())

if b >= c:
    print(-1)
else : 
    n = int(a/(c-b))+1
    print(n)     