'''

문제 설명
숫자 a, b가 주어졌을 때 a를 b로 나눈 몫과 a를 b로 나눈 나머지를 공백으로 구분해 출력해보세요.

입력 설명
입력으로는 공백으로 구분된 숫자가 두 개 주어집니다.
첫 번째 숫자는 a를 나타내며, 두 번째 숫자는 b를 나타냅니다.

출력 설명
a를 b로 나눈 몫과 a를 b로 나눈 나머지를 공백으로 구분해 출력하세요.

제한 조건
a와 b는 자연수입니다.
입력 예
5 3
출력 예
1 2

'''

a, b = map(int, input().strip().split(' '))


# input으로 받은 값을 strip()을 통하여 양쪽 공백을 지우고
# .split('')을 가지고 띄어쓰기를 기준으로 문자열을 나눴다.

def number_arithmetic_operation(a, b):
    c = a // b
    d = a % b
    print('{} {}'.format(c, d))


number_arithmetic_operation(a, b)

# a = 7
# b = 5
# print(a//b, a%b)

# a = 7
# b = 5
# print(*divmod(a, b))