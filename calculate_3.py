money, c500 ,c100, c50, c10 = 0,0,0,0,0
money =int(input("교환돈 얼마?"))

c500 = money // 500
money %= 500

c100 = money // 100
money %= 100

c50 = money // 50
money %= 50

c10 = money // 10
money %= 10

print( "\n 500원짜리  ==> %d개 " % c500)        #3가지 방법  print("{}" % fomat(x)) ,print("{}" % fomat(x)), print(f"{x}")리터럴   
print( "100원짜리  ==> %d개 " % c100)
print( "50원짜리  ==> %d개 " % c50)
print( "10원짜리  ==> %d개 " % c10)
print( "바꾸지 못한 잔돈  ==> %d 원 " % money)