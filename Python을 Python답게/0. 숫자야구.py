import random

print("=" * 45)
print("도전! 숫자야구".center(38))
print("=" * 45)
print("")

trial = 0
strike_new = 0

length = int(input("""난이도를 설정합니다!
3~5사이의 자릿수를 숫자로 입력하세요 : """))
while True:
    if length < 3 or length > 5:
        length = int(input("3~5사이의 숫자만 가능합니다 : "))
    else:
        break

password = random.sample(range(0, 10), length)

while True:

    for x in range(length):
        for y in range(length):
            answer = input("중복되지 않는 " + str(length) + "자리 숫자를 입력하세요 : ")
            if int(answer[x]) == int(answer[y]) and x != y:
                answer = input("중복되는 수가 있습니다. 다시 입력해주세요 : ")
            elif int(len(answer)) != length:
                answer = input(str(length) + "자리 숫자가 아닙니다. 다시 입력해주세요 : ")
            else:
                strike = 0
                ball = 0
                out = 0

                for i in range(length):
                    for j in range(length):
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

                if strike == length:
                    strike_new += strike

    if strike_new == length:
        break

print("")
print("=" * 45)
print("게임종료")
print("정답은 : " + ''.join(list(map(str, password))) + "입니다.")
print("총 " + str(trial) + "번 시도하셨습니다.")
print("=" * 45)