a = input("시작수(큰수):")
b = input("끝수(작은수):")
int_a = int(a)
int_b = int(b)


arr = range(int_a,int_b-1,-1)

for i in arr:
    print(i)

