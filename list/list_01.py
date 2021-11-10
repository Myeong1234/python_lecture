aa = [ 0, 0, 0, 0]
hap = 0

for i in range(len(aa)) :
    aa[i] = int(input(f"{i+1}번째 숫자 : "))
    hap += aa[i]

print(f"합계 {hap}")