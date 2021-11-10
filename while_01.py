# #while문
# i=0
# while i<3 :
#     print(f"{i}안녕하세요 while문 공부중입니다. ^^ ")
#     i += 1


ch , ch1 = '', ''
a,b = 0, 0 

while True :
    a = int(input("계산할 첫번째 숫자 : "))
    b = int(input("계산할 두번째 숫자 : "))
    ch = input("계산할 연산자 : ")

    
    if (ch == "+") :
        print(f"{a} + {b} = {a + b}")
    elif (ch == "-") :
        print(f"{a} - {b} = {a - b}")
    elif (ch == "*") :
        print(f"{a} * {b} = {a * b}")
    elif (ch == "/") :
        print(f"{a} / {b} = {a / b}")
    elif (ch == "%") :
        print(f"{a} % {b} = {a % b}")
    elif (ch == "//") :
        print(f"{a} // {b} = {a // b}")
    elif (ch == "**") :
        print(f"{a} ** {b} = {a ** b}")
    else :
        print("연산자를 잘못입력하였습니다.")

    ch = input("끝내려면 q 아니면 아무거나 입력 ")
    if (ch1 == 'q') :
        break;
