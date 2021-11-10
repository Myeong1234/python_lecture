#1번
# for i in ("a",1, "와") :
#     print("나와라~")

# for i in range(1,5):
#     print("잠이 깬다")

#2번
# for i in range(0,10,2):
#     print(f"잠이 깬다 {i}")



#3번
# a=0
# for i in range(1,11):
#     a += i
#     print(f"{a}")

#4번 string도 가능
# ord() 문자를 아스키코드로 변환, chr()  아스키코드를 문자로 변환

# for i in "Hello World" :
#     # if i != "H" or i !='w' :
#     #     print(i)
#     if ord(i) >= 65 and ord(i) <= 90 :
#         continue
#     else :
#         print(i)
# print(len("hello world"))


#5번
i, hap = 0,0

for i in range(501 , 1001, 2) :
    hap = hap + i 

print(f"500과 1000사이에 있는 홀수의 합계 {hap}")
