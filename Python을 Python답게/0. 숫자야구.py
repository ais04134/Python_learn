import random

print("=" * 30)
print("도전! 숫자야구".center(23))
print("=" * 30)
print("")

trial = 0

password = random.sample(range(0, 10), 3)

while True:

    answer = input("중복되지 않는 3자리 숫자를 입력하세요 : ")
    while answer[0] == answer[1] or answer[1] == answer[2] or answer[0] == answer[2]:
        answer = input("중복되는 수가 있습니다. 다시 입력해주세요 : ")
        while int(len(answer)) != 3:
            answer = input("3자리 숫자가 아닙니다. 다시 입력해주세요 : ")

    strike = 0
    ball = 0
    out = 0

    for i in range(3):
        for j in range(3):
            if int(answer[i]) == int(password[j]) and i == j:
                strike = strike + 1
            elif int(answer[i]) == int(password[j]) and i != j:
                ball = ball + 1
    if int(ball) == 0 and int(strike) == 0:
        out = 1

    trial = trial + 1

    print(str(strike) + " strike")
    print(str(ball) + " ball")
    print(str(out) + " out")
    print(str(trial) + "번 시도함")