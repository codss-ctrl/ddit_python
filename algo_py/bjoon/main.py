import numpy as np
# def solve(a):
#     sum = 0
#     for i in a:
#         sum += i
#     return sum   
# 
# #숏코딩
# def solve(a):
#     return sum(a)
# 

# def d(n):
#     result = n
#     while n!= 0:
#         result += n%10
#         n//=10
#     return result
# list1 = []
# 
# for i in list(range(1,10001)):
#     list1.append(d(i))
#     if i not in list1:
#         print(i)    
#         
# ################################
# 
# num_set1 = set(range(1,10001))
# num_set2 = set()
# 
# for i in range(1,10001):
#     for j in str(i):
#         i += int(j)
#     num_set2.add(i)
# self_num_set = num_set1-num_set2
# 
# for i in sorted(self_num_set):
#     print(i)    
#     
# ########
# r=range(9999);print(*sorted({*r}-{n+sum(map(int,str(n)))for n in r}))

# cnt = input()
# num = list(map(int, input().split()))
# nump = np.array(num)
# M = max(nump)
# nnump = nump/M*100
# aveg = sum(nnump)/nump.size
# print(aveg)
# 
# cnt = int(input())
# num = list(map(int, input().split()))
# 
# M = max(num)
# result = 0
# 
# for i in num:
#     result += i / M * 100
# ans = result /cnt    
# print(ans)

c = int(input()) #테스트 케이스 수
result = 0 # 평균
list1 = list(map(int, input().split()))#학생 수[0] , 학생들의 점수[1]~[끝]
for i in range(1,list1[0]+1):
    result += round(list1[i]/list1[0],3)
    print(result)
















 