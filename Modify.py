import random

def playgame(rannum, count, maxcount):
    while True:
        try:
            answer = int(input("숫자를 입력해주세요.\n"))

            if answer > rannum:
                print("입력한 숫자가 정답보다 큽니다.")
                print("시도 횟수:", count)
                count += 1
            elif answer < rannum:
                print("입력한 숫자가 정답보다 작습니다.")
                print("시도 횟수:", count)
                count += 1
            elif answer == rannum:
                print("정답입니다! 프로그램을 종료합니다.")
                print("시도 횟수:", count)
                quit()

        except ValueError:
            print("숫자를 입력해주셔야 합니다.")

        if count == maxcount:
            print("시도 횟수를 모두 소진했습니다. 프로그램을 종료합니다.")
            quit()

def gamestart():
    start = input("숫자 맞추기 게임에 오신 것을 환영합니다!\n메뉴를 숫자로 선택해주세요. 프로그램 종료를 원하시면 메뉴 번호를 제외한 아무거나 입력하시면 됩니다.\n1. 쉬움(1 ~ 50, 횟수 제한 20)\n2. 보통(1 ~ 100, 횟수 제한 10)\n3. 어려움(1 ~ 1000, 횟수 제한 15)\n")
    if start == "1":
        print("쉬움 난이도를 시작합니다.")
        playgame(random.randrange(1, 51), 1, 20)
    if start == "2":
        print("보통 난이도를 시작합니다.")
        playgame(random.randrange(1, 101), 1, 10)
    if start == "3":
        print("어려움 난이도를 시작합니다.")
        playgame(random.randrange(1, 1001), 1, 15)
    else:
        print("프로그램을 종료합니다.")

gamestart()
