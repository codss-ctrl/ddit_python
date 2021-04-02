import sys

c = int(input())  # 테스트 케이스의 개수 C

for _ in range(c):  # c 수 만큼 반복
    a = list(map(int,sys.stdin.readline().split()))  # 첫 수 : 학생의 수 , N명의 점수
    cnt = 0  # 평균을 넘는 학생 수
    avg = sum(a[1:])/a[0]  # 평균
    for score in a[1:]:
        if score > avg:
            cnt += 1  # 평균을 넘는 학생 수
    rate = cnt/a[0]*100 # 평균을 넘는 학생들의 비율
    print(f'{rate:.3f}%')
