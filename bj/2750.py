# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다.
# 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

N = int(input())  # 주어질 수의 개수를 입력 받는다.
list2 = []
for i in range(N):  # N번 만큼 반복하여
    list2.append(int(input()))  # 각각의 수를 추가
list2.sort()  # 정렬
for i in list2:
    print(i)  # 하나씩 출력
