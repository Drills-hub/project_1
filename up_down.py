import random

random_num = random.randint(1, 100)

print("up-down 게임을 시작합니다.")
print("수의 범위는 1-100 입니다.")

count = 0
score = []

# 최고 점수 반환


def high_score(scores):
    return min(scores)


while True:
    num = input("숫자를 입력하세요: ")

    # 문자열 데이터를 입력할 경우 에러 방지

    try:
        num_user = int(num)

    except ValueError:
        print("숫자가 아닙니다.")
        continue

# 범위 안의 숫자를 쓰게 유도

    if 0 > num_user or 100 < num_user:
        print("1-100 까지의 숫자 중 입력하세요")
        continue

    elif 0 < num_user < 101:

        if num_user < random_num:
            print("UP!")
            count += 1
            continue

        elif num_user > random_num:
            print("Down!")
            count += 1
            continue

        # 정답을 맞춘 뒤 다시 시작을 질문
        elif num_user == random_num:
            score.append(count+1)
            print(f"축합니다. 정답입니다! {count+1}번 만에 맞추셨습니다!! ")
            print(f" 최고 기록은 {high_score(score)} 입니다.")
            restart = input("다시 시작 하시겠습니까?(y/n): ").lower()
            count = 0

            if restart == "n":
                break
            elif restart == "y":
                random_num = random.randint(1, 100)
                continue
            else:
                print(f"다시 선택해 주세요")
                restart = input("다시 시작 하시겠습니까?(y/n): ").lower()

                if restart == "n":
                    break

                elif restart == "y":
                    random_num = random.randint(1, 100)
                    continue

                else:
                    print("게임을 종료하겠습니다")
                    break
