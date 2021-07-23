'''

모든 멤버의 type 변환하기
문제 설명
문자열 리스트 mylist를 입력받아, 이 리스트를 정수형 리스트로 바꾼 값을 리턴하는 함수, solution을 만들어주세요. 예를 들어 mylist가 ['1', '100', '33'] 인 경우, solution 함수는 [1, 100, 33] 을 리턴하면 됩니다.

제한조건
mylist의 길이는 100 이하인 자연수입니다.
mylist의 원소는 10진수 숫자로 표현할 수 있는 문자열입니다. 즉, 'as2' 와 같은 문자열은 들어있지 않습니다.
예시
input	output
['1', '100', '33']	[1, 100, 33]

'''

# def solution(mylist):
#     answer = []
#     for i in mylist:
#         answer.append(int(i))
#     return answer

list1 = ['1', '100', '33']
list2 = list(map(int, list1))

'''

map 함수 응용하기
문제 설명
정수를 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다. solution 함수가 mylist 각 원소의 길이를 담은 리스트를 리턴하도록 빈칸을 완성해보세요.

hint) 이전 강의에서 배운 map 함수를 활용해보세요

제한 조건
mylist의 길이는 100 이하인 자연수입니다.
mylist 각 원소의 길이는 100 이하인 자연수입니다.
예시
input	output
[[1], [2]]	[1, 1]
[[1, 2], [3, 4], [5]]	[2, 2, 1]

'''

def solution(mylist):
    answer = list(map(len, mylist))
    return answer