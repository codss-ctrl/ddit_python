a = input("a=")
b = input("b=")
print(a+"에서 "+b+"까지 합은")

int_a = int(a)
int_b = int(b)

arr = range(int_a,int_b+1)

sum = 0
for i in arr:
    sum += i

print(sum)


