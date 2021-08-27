# Chapter03-02
# Special Method(Magic Method)
# Python의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), Class(클래스)

# Class안에 정의할 수 있는 특별한(빌트인-> 이미 만들어 둔) 메소드가 Special 메소드 (Magic 메소드) <-- __init__ 같은것


# 기본형
print(int)
print(float)

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

n = 10

print(type(n)) # 우리가 사소하게 사용하였던 변수 하나도 Class로 이루어져 있다.

print( n + 100) # __add__ 가 호출 된것임
print(n.__add__(100))
# print(n.__doc__) <- 설명문 읽는 방법

print(n.__bool__(), bool(n))
print(n*100, n.__mul__(100))

print()
print()

# Class 예제1
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit Class Info : {} , {}'.format(self._name, self._price) # 인스턴스 변수에 대한 설명

    def __add__(self, other):
        # 이렇게 만들었는 __add__ 매직메서드가 진짜 호출 되는지 확인해보고 어떻게 응용할 수 있을지 생각해보자
        print("__add__ 이거 호출되나?")
        return (self._price + other._price)*0.8 # 이런식으로 기존에 정의된 덧샘 메소드를 수정할 수 있다.

    def __sub__(self, other):
        print('Called >> __sub__')
        return self._price - other._price

    def __le__(self, other):
        print('Called >> __le__')
        if self._price <= other._price:
            return True
        else:
            return False

    def __ge__(self, other):
        print('Called >> __ge__')
        if self._price >= other._price:
            return True
        else:
            return False


# 인스턴스 생성

s1 = Fruit('Orage', 7500)
s2 = Fruit('Banana', 3000)

print(s1 + s2)

# 일반적인 계산
# print(s1._price _ s2._price)

# 매직메소드
print(s1 >= s2)
print()

print(s1 <= s2)
print()

print(s1 - s2)
print()

print(s2 - s1)
print()

print(s1)
print()

print(s2)

# 기존에 있던 매직메소드들을 수정하여 커스터마이징 할 수 있다.

# Class 예제2
# 벡터(x,y) (5,2) + (4,3) = (9, 5)
# (10, 3)*5 = (50, 15)
# Max((5, 10)) = 10

class Vector(object):
    def __init__(self, *args): # __init__(self, x, y) <- 이런식으로 하는 것 보다 패킹의 방식을 활용해 보자
        '''
        Create a vector, example : v = Vector(5, 10)
        '''

        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        '''Return the vector infomations.'''
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __add__(self, other): # __add__ 메서드가 나의 목적에 맞게 새롭게 구현되었다.
        '''Return the vector addtion of self and other'''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        '''좌표 평면상에 (0,0)에 있는지 반환하는 함수'''
        return bool(max(self._x, self._y)) # 만약, max(5)가 들어오면 -> bool(5)로 들어오고 이 값이 0 보다 크므로 True로 나온다.


print(Vector.__init__.__doc__) # __init__ 의 주석의 경우에는 이런식으로 알아볼 수 있다.
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)


v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()

# 매직매소드 출력

print(Vector.__init__.__doc__) # __init__ 의 주석의 경우에는 이런식으로 알아볼 수 있다.
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)

print(v1, v2, v3)
print()

print(v1 + v2) # __add__ 메서드가 나의 목적에 맞게 새롭게 구현되었다.
print()

print(v1 *3)
print()

print(v2*10)
print()

print(bool(v1), bool(v2))
print()

print(bool(v3))

# 우리가 평소에 쓰는 사칙연산에 대한 커스터마이징을 할 수 있다. <- 큰 프로젝트에 사용할 수 있다면 편리할듯?..


# Chapter03-03
# Special Method(Magic Method)
# Python의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), Class(클래스)

# Class안에 정의할 수 있는 특별한(빌트인-> 이미 만들어 둔) 메소드가 Special 메소드 (Magic 메소드) <-- __init__ 같은것

# 객체 -> Python의 데이터를 추상화
# 모든 객체 -> id, type -> value

# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

l_leng1 = sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2) # 두 점 사이의 거리 공식

print(l_leng1)

# 네임드 튜플

from collections import namedtuple


#  네임드 튜플 선언
Point = namedtuple('Point','x y') # namedtuple을 사용하면 데이터의 구조를 좀 더 쉽게 파악하고 활용할 수 있다.

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(pt3, pt4)

# l_leng2 = sqrt((pt3[0] - pt4[0])**2 + (pt3[1] - pt4[1])**2)
# 이런식으로 인덱스로 접근하는 것을 키로 접근할 수 있다.

l_leng2 = sqrt((pt3.x - pt4.x)**2 + (pt3.y - pt4.y)**2) # 이런식으로 namedtuple을 활용하여 key값으로도 접근 가능하다.

print(l_leng2)

# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename = True) # Default = False <- 따라서 중복이나 등등 에러가 나왔던 것

# 출력
print(Point1, Point2, Point3, Point4)

# Dict to Unpacking
temp_dict = {'x': 75, 'y': 55}

# 객체 생성
p1 = Point1(x= 10, y= 35)
p2 = Point2(20, 40)
p3 = Point3(45, y = 20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict) # 우어어어ㅓ 신기해 신기해

print()

print(p1)
print(p2)
print(p3)

# rename 테스트
print(p4) # 중복값과 예약어를 알아서 변수로 변환하여 저장한다. <- 궂이 이렇게 사용할 필요가 있을까???
print(p5)

# 사용
print(p1.x + p2.y)

# Unpacking
x, y = p3

print(x, y)

# 네임드 튜플 메소드
temp = [52, 38]

# _make() : 새로운 객체 생성
p4 = Point1._make(temp)

print(p4)

# _fields : 필드 네임 확인
print(p1._fields, p2._fields, p3._fields)

# _asdict() : OrderedDict 반환
print(p1._asdict())


# 실 사용 실습
# 반 20명, 4개의 반(A, B, C, D)

Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언

numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()

print(numbers)
print(ranks)

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]

print(students)

# 추천
students2 = [
    Classes(rank, number)
    for rank in 'A B C D'.split()
        for number in [str(n)
            for n in range(1, 21)]
]  # 이런식으로 코드 짜는건 안갈켜줬잖아...

print(students2)

# 출력
for s in students2:
    print(s)