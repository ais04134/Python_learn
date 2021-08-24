# Chapter02-01
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 과거에는 함수 중심으로 코딩 되었다. -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

# 일반적인 코딩

# 차량1
cor_company_1 = 'Ferrari'
car_detail_1 = [
    {'color' : 'White'},
    {'horsepower' : 400},
    {'price' : 8000}
]

# 차량2
cor_company_2 = 'Bmw'
car_detail_2 = [
    {'color' : 'Black'},
    {'horsepower' : 270},
    {'price' : 5000}
]

# 차량3
cor_company_3 = 'Audi'
car_detail_3 = [
    {'color' : 'Silver'},
    {'horsepower' : 300},
    {'price' : 6000}
]

# 리스트 구조
# 관리하기가 불편하다.
# 인덱스 접근 시 실수 가능성, 삭제 불편
car_company_list = ['Ferrari','Bmw', 'Audi']
car_detail_list = [
    {'color' : 'White', 'horsepower' : 400, 'price' : 8000},
    {'color' : 'Black', 'horsepower' : 270, 'price' : 5000},
    {'color' : 'Silver', 'horsepower' : 300, 'price' : 6000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print()
print()


# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키), 키 조회 예외 처리 등

car_dicts = [
    {'car_company': 'Ferrai', 'car_detail': {'color' : 'White', 'horsepower' : 400, 'price' : 8000}},
    {'car_company': 'Bmw', 'car_detail': {'color' : 'Black', 'horsepower' : 270, 'price' : 5000}},
    {'car_company': 'Audi', 'car_detail': {'color' : 'Silver', 'horsepower' : 300, 'price' : 6000}}
]

print(car_dicts)

# pop(key, 'default')
del car_dicts[1]
print(car_dicts)

print()
print()

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

class Car():
    def __init__(self,company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return 'str: {}-{}'.format(self._company,self._details)

    def __repr__(self):
        return 'repr: {}-{}'.format(self._company,self._details)

    def __reduce__(self):
        pass

car1 = Car('Ferrari', {'car_company': 'Ferrai', 'car_detail': {'color' : 'White', 'horsepower' : 400, 'price' : 8000}})
car2 = Car('Bmw', {'car_company': 'Bmw', 'car_detail': {'color' : 'Black', 'horsepower' : 270, 'price' : 5000}})
car3 = Car('Audi', {'car_company': 'Audi', 'car_detail': {'color' : 'Silver', 'horsepower' : 300, 'price' : 6000}})

print(car1)
print(car2)
print(car3)

print(car1.__dict__) # __dict__이라는 일반 속성으로 접근을 하면 속성 값들을 전부 볼 수 있다.

print(dir(car1))# dir을 통해서 이 안에 있는 모든 메타정보를 확인할 수 있다.

print()
print()

# 리스트 선언
car_list = []

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

# 반복(__str__)
for i in car_list:
    print(repr(i))
    print(i)


# Chapter02-02
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 과거에는 함수 중심으로 코딩 되었다. -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car_ver2():
    '''
    Car_ver2 class
    Author : PARK
    Date : 2021.08.25
    사용법 : ~~~
    ~~~ 

    ''' # 주석을 달아야 하는 이유를 __doc__를 통하여 설명해 주셨다.

    # 클래스 변수(모든 인스턴스가 공유한다.)
    car_count = 0


    def __init__(self,company, details):
        self._company = company # _ <- 를 하나 붙히는 이유는 인스턴스 변수임을 나타내는 것
        self._details = details
        Car_ver2.car_count += 1 # __init__ 메서드가 호출될 때 마다 클레스 변수의 값이 1식 증가하게 된다.

    def __str__(self):
        return 'str: {}-{}'.format(self._company,self._details)

    # def __del__(self):
    #     print('호출이 되는 건가 ??')
    #     Car.car_count -= 1

    def __repr__(self):
        return 'repr: {}-{}'.format(self._company,self._details)

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

# Self 의미
car_ver2_1 = Car_ver2('Ferrari', {'color' : 'White', 'horsepower' : 400, 'price' : 8000})
car_ver2_2 = Car_ver2('Bmw', {'color' : 'Black', 'horsepower' : 270, 'price' : 5000})
car_ver2_3 = Car_ver2('Audi', {'color' : 'Silver', 'horsepower' : 300, 'price' : 6000})

# ID 확인
print(id(car_ver2_1))
print(id(car_ver2_2))
print(id(car_ver2_3))

print(car_ver2_1._company == car_ver2_2._company)
print(car_ver2_1 is car_ver2_2)

# dir & __dict__ 확인
print(dir(car_ver2_1)) # 해당 인스턴스가 가지고 있는 모든 속성들을 리스트 형태로 보여준다.
print(dir(car_ver2_2))

print()
print()

print(car_ver2_1.__dict__) # 모든 속성들이 아니라, 인스턴스 안에 있는 세부적인 값을 보여준다.
print(car_ver2_2.__dict__)

# Doctring
print(car_ver2_1.__doc__) # 앞서 ''' 사용법~~~ ''' 이런식으로 적었던 설명문을 출력해 준다.
print()

# 실행
car_ver2_1.detail_info()
car_ver2_2.detail_info()

# 비교
print(car_ver2_1.__class__, car_ver2_2.__class__) # 같은 class에서 나온 것을 알 수 있다.

# 같은 객체임을 알 수 있다. 인스턴스 객체 값은 다르겠지만 같은 class에서 나왔으므로 class에 대한 객체 값은 동일함을 알 수 있다.
print(id(car_ver2_1.__class__), id(car_ver2_2.__class__))


# 에러
# Car_ver2.detail_info() # 클레스로 접근을 하면 에러가 난다.
# Car_ver2.detail_info(car_ver2_1) # slef인자를 붙여 줘야한다.

# 공유확인
print(car_ver2_1.car_count)
print(car_ver2_2.car_count) # 클래스 변수 값은 공유하고 있음을 알 수 있다.
print(car_ver2_1.__dict__)
print(car_ver2_2.__dict__) # 클래스 변수 값은 나오지 않고 인스턴스 변수값들을 자세하게 설명해 준다.
print(dir(car_ver2_1)) # 클래스 변수까지 보여준다.

# 접근
print(car_ver2_1.car_count)
print(Car_ver2.car_count)

del car_ver2_2

# 삭제 확인
print(car_ver2_1.car_count)
print(Car_ver2.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))



class Car_ver3():
    '''
    Car_ver2 class
    Author : PARK
    Date : 2021.08.25
    Description : Class, Static, Instance Method
    ~~~ 

    ''' # 주석을 달아야 하는 이유를 __doc__를 통하여 설명해 주셨다.

    # 클래스 변수(모든 인스턴스가 공유한다.)
    price_per_raise = 1.0

    def __init__(self,company, details):
        self._company = company # _ <- 를 하나 붙히는 이유는 인스턴스 변수임을 나타내는 것
        self._details = details

    def __str__(self):
        return 'str: {}-{}'.format(self._company,self._details)

    def __repr__(self):
        return 'repr: {}-{}'.format(self._company,self._details)

    # Instance Method
    # Self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    # Instance Method
    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))

    # Instance Method
    def get_price_culc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price')*Car_ver3.price_per_raise)

    # Class Method
    # 클래스 변수를 읽어오거나 값을 변경하거나 할때 사용한다.
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 Or More')
            return
        cls.price_per_raise = per
        print('Succeed! price increased.')


# Self 의미
car_ver3_1 = Car_ver3('Ferrari', {'color' : 'White', 'horsepower' : 400, 'price' : 8000})
car_ver3_2 = Car_ver3('Bmw', {'color' : 'Black', 'horsepower' : 270, 'price' : 5000})

# 전체정보
car_ver3_1.detail_info()
car_ver3_2.detail_info()

#가격정보(직접 접근)
print(car_ver3_1._details.get('price'))

# 가격정보(인상전)
print(car_ver3_1.get_price())
print(car_ver3_2.get_price())

# 가격 인상(클래스 메소드 미사용)
Car_ver3.price_per_raise = 1.4

# 가격정보(인상 후)
print(car_ver3_1.get_price_culc())
print(car_ver3_2.get_price_culc())

# -------------------------------------------

# 가격정보(인상전)
print(car_ver3_1.get_price())
print(car_ver3_2.get_price())

# 가격 인상(클래스 메소드 사용)
Car_ver3.raise_price(1.6)

# 가격정보(인상 후)
print(car_ver3_1.get_price_culc())
print(car_ver3_2.get_price_culc())