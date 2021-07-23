'''

정수를 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다. mylist에 들은 각 원소의 길이를 담은 리스트를 리턴하도록 solution 함수를 작성해주세요.

<제한 조건>
mylist의 길이는 100 이하인 자연수입니다.
mylist 각 원소의 길이는 100 이하인 자연수입니다.

<예시>
input	                 output
[[1], [2]]	             [1,1]
[[1, 2], [3, 4], [5]]	 [2,2,1]


'''

def solution(mylist):
    C = []
    for i in range(len(mylist)):
        B = len(mylist[i])
        C.append(B)
    answer = C
    return answer

mylist = [[1,3], [4,3], [1,2,4,5,3]]

solution(mylist)

# def solution(my_list)
#     return list(map(len, my_list))