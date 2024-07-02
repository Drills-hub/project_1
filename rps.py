import random

choice_rps = ["가위", "바위", "보"]

com_choice = random.choice(choice_rps)

win = 0
lose = 0
draw = 0

print("가위바위보 게임을 시작하겠습니다.")

while True:
    user_choice = input(f"가위,바위,보 중 입력하세요: ").lower()

    if user_choice not in choice_rps:
        print("다시 입력 하세요")
        continue

    if user_choice == com_choice:
        draw += 1
        print(f"비겼습니다!")
        print(f"전적은 win:{win}, lose:{lose}, draw: {draw} 입니다. ")
        restart = input("다시 시작 하시겠습니까?(y/n): ").lower()

        if restart == "n":
            break

        elif restart == "y":
            continue

        else:
            print("게임을 종료하겠습니다")
            break

    elif (user_choice == "주먹" and com_choice == "가위") or \
        (user_choice == "가위" and com_choice == "보") or \
            (user_choice == "보" and com_choice == "바위"):

        win += 1
        print(f"유저가 이겼습니다!")
        print(f"전적은 win:{win}, lose:{lose}, draw: {draw} 입니다. ")
        restart = input("다시 시작 하시겠습니까?(y/n): ").lower()

        if restart == "n":
            break

        elif restart == "y":
            continue

        else:
            print("게임을 종료하겠습니다")
            break
    else:
        lose += 1
        print(f"유저가 졌습니다!")
        print(f"전적은 win:{win}, lose:{lose}, draw: {draw} 입니다. ")
        restart = input("다시 시작 하시겠습니까?(y/n): ").lower()

        if restart == "n":
            break

        elif restart == "y":
            continue

        else:
            print("게임을 종료하겠습니다")
            break
