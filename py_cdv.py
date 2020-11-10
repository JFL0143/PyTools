# PyCpv a201110
def run():
    def cpv():
        def calculate():
            while True:
                try:
                    op = input("덧셈 or 뺄셈 or 곱셈 or 나눗셈을 입력해주세요: ")
                    if op == "종료":
                        break
                    elif op != "덧셈" and op != "뺄셈" and op != "곱셈" and op != "나눗셈":
                        raise SyntaxError
                    num1 = input("첫번째 수를 입력해주세요. ")
                    if num1 == "종료":
                        break
                    num1 = int(num1)
                    num2 = input("두번째 수를 입력해주세요. ")
                    result = None
                    if num2 == "종료":
                        break
                    num2 = int(num2)
                    if op == "덧셈":
                       result = num1 + num2
                    elif op == "뺄셈":
                        result = num1 - num2
                    elif op == "곱셈":
                        result = num1 * num2
                    elif op == "나눗셈":
                        if num2 == 0:
                            print("0으로 나눌 수 없습니다.")
                        else:
                            result = num1 / num2
                    print("결과는 {} 입니다".format(result))
                    print("계산을 계속하시겠습니까?")
                    ox = input("> ")
                    if ox == "X":
                       return None
                    elif ox != "O":
                        raise TypeError
                except Exception:
                    print("오류가 발생했습니다.")
        def echo():
            while True:
                메시지 = message()
                if 메시지 == "종료":
                    break
                print(메시지)
        def message():
            메시지 = input("메시지를 입력해주세요: ")
            return 메시지
        def reverse():
            while True:
                lst = list(message())
                k = len(lst) // 2
                for i in range(k):
                    temp = lst[i]
                    lst[i] = lst[-(1 + i)]
                    lst[-(1 + i)] = temp
                text = ""
                for i in range(len(lst)):
                    text = text + lst[i]
                print(text)
        def binary_to_decimal():
            arr = list(message())
            num = 0
            for i in range(len(arr)):
                if arr[-(i+1)] == "1":
                    num += (2 ** i)
                elif arr[-(i+1)] != "0":
                    raise TypeError
            print(num)
        def start():
            message = input("""봇을 선택해주세요.""")
            if message == "초파봇":
                print("네, 알겠습니다.")
                try:
                    print("초파봇이 정상적으로 실행되었습니다.")
                except:
                    print("초파봇 실행 중 오류가 발생했습니다.")
                print("초! (코!!) 파!!! (이!!!!) 봇!!!!!")
                menu = input("""초파봇 메뉴:
커맨드
> """)      
            elif message == "저장":

                if menu == "커맨드":
                    print("OK!")
                    try:
                        print("실행완료!")
                    except:
                        print("오류발새애애애앵!!!")
                    print("초파봇 커맨드 목록{형식: (커맨드 " + """이름)(num), 커맨드 실행: num 입력}: 
(참고) 메시지 입력 시('메시지를 입력해주세요: ' 나왔을 때!) '종료'를 입력하면 커맨드 종료(일부 예외 커맨드 제외)
따라하기(0): 말을 따라함.
초기화(1): 챗봇 초기화(위험!)
계산(2): 현재 사칙연산 가능.
리버스(3): 말 그대로 리버스(cat > tac, rainbow > wobniar, 고기는맛있어 > 어있맛는기고, ...)(현재 예외)
2진수 > 10진수 변환(4): 신규기능.
---B35---""")
                    while True:
                        모드 = input("모드를 선택해주세요: ")
                        if 모드 == "0":
                            echo()
                        elif 모드 == "1":
                            ox = input("정말로 초기화하시겠습니까: ")
                            if ox == "O":
                                return None
                            elif ox == "X":
                                print("취소되었습니다.")
                        elif 모드 == "2":
                            calculate()
                        elif 모드 == "3":
                            reverse()
                        elif 모드 == "4":
                            binary_to_decimal()
                        elif 모드 == "5":
                            pass
                            # decimal_to_binary()
    print("안녕하세요. 가이드봇입니다.")
    사용자명 = input("사용자명을 입력해주세요: ")
while True:
    run()