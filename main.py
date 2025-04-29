import random

while True:
    start = input("게임을 시작하겠습니까? 시작:네 종료:아니오\n")
    
    if start == "네":
        while True:
            level = input("난이도를 결정해주세요. \n1. 쉬움(1 ~ 50, 횟수 제한 20) \n2. 보통(1 ~ 100, 횟수 제한 10) \n3. 어려움(1 ~ 1000, 횟수 제한 10)\n")
            if level == "1":
                print("쉬움 난이도를 시작합니다")

                easynum = random.randrange(1, 51)
                easytrynum = 1

                while True:
                    try:
                        answer = int(input("숫자를 입력해주세요."))

                        if answer < easynum:
                            print("입력한 숫자가 정답보다 작습니다.")
                            print("시도 횟수:", easytrynum)
                            easytrynum += 1
                        elif answer > easynum:
                            print("입력한 숫자가 정답보다 큽니다.")
                            print("시도 횟수:", easytrynum)
                            easytrynum += 1
                        elif answer == easynum:
                            print("정답입니다! 프로그램을 종료합니다.")
                            print("시도 횟수:", easytrynum)
                            quit()

                    except ValueError:
                        print("올바른 값을 입력해주세요.")
                    
                    if easytrynum == 21:
                        print("시도 횟수를 모두 소진했습니다. 프로그램을 종료합니다.")
                        quit()

            elif level == "2":
                print("보통 난이도를 시작합니다.")

                nomalnum = random.randrange(1, 101)
                nomaltrynum = 1

                while True:
                    try:
                        answer = int(input("숫자를 입력해주세요."))

                        if answer < nomalnum:
                            print("입력한 숫자가 정답보다 작습니다.")
                            print("시도 횟수:", nomaltrynum)
                            nomaltrynum += 1
                        elif answer > nomalnum:
                            print("입력한 숫자가 정답보다 큽니다.")
                            print("시도 횟수:", nomaltrynum)
                            nomaltrynum += 1
                        elif answer == nomalnum:
                            print("정답입니다! 프로그램을 종료합니다.")
                            print("시도 횟수:", nomaltrynum)
                            quit()

                    except ValueError:
                        print("올바른 값을 입력해주세요.")
                    
                    if nomaltrynum == 11:
                        print("시도 횟수를 모두 소진했습니다. 프로그램을 종료합니다.")
                        quit()

            elif level == "3":
                print("어려움 난이도를 시작합니다.")

                hardnum = random.randrange(1, 1001)
                hardtrynum = 1

                while True:
                    try:
                        answer = int(input("숫자를 입력해주세요."))

                        if answer < hardnum:
                            print("입력한 숫자가 정답보다 작습니다.")
                            print("시도 횟수:", hardtrynum)
                            hardtrynum += 1
                        elif answer > hardnum:
                            print("입력한 숫자가 정답보다 큽니다.")
                            print("시도 횟수:", hardtrynum)
                            hardtrynum += 1
                        elif answer == hardnum:
                            print("정답입니다! 프로그램을 종료합니다.")
                            print("시도 횟수:", hardtrynum)
                            quit()

                    except ValueError:
                        print("올바른 값을 입력해주세요.")
                    
                    if hardtrynum == 11:
                        print("시도 횟수를 모두 소진했습니다. 프로그램을 종료합니다.")
                        quit()
                

    elif start == "아니오":
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 값을 입력해주세요.")