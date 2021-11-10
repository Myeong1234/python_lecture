#2중 for문
# for i in range(0,3) :
#     for k in range(0,2) :
#         print(f"파이썬은 꿀잼입니다.^^ (i값 : {i}, k값 : {k})")

#구구단
# for i in range(1,10) :
#     print(f"{i}단")
#     for k in range(1,10) :
#         print(f"구구단 {i} X {k} = {i*k}")

a = 0
hap =0

temp = [ i for i in range(10, 20) if i % 2 == 1]

for i in range(len(temp)):
    hap += temp[i]

print(f"500과 1000사이에 있는 홀수의 합계 : {hap}")
