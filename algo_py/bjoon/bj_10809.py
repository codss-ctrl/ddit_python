s=list(input())
arr = []
for i in range(97,123):#ord(a)=97,ord(z)=123
    a = chr(i)
    if s.count(a)==0:
        arr.append('-1')
    else :
        arr.append(str(s.index(a)))    
for i in arr:
    print(i,end=" ")        