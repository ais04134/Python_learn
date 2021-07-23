'''

문제 설명
입력으로 0이 주어지면 영문 소문자 알파벳을, 입력으로 1이 주어지면 영문 대문자 알파벳을 사전 순으로 출력하는 코드를 짜세요.

예시 1
입력

0
출력

abcd...(중간생략)..xyz
예시 2
입력

1
출력

ABCD...(중간생략)..XYZ

'''

num = int(input().strip())

if num == 0:
    print('abcdefghijklmnopqrstuvwxyz')
else :
    print('ABCDEFGHIJKLMNOPQRSTUVWXYZ')