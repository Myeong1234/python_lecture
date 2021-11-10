# aa = []
# bb = []
# value = 0

# for _ in range(0, 100) :
#     aa.append(0)
#     value += 2

# for i in range(0,100) :
#     bb.append(aa[99-i])

# print(f"bb[0]에는 {bb[0]} 이 , bb[99]에는 {bb[99]}입력됩니다.")

aa = [10 , 20, 30, [40, 50, 50, 60] ]
ab = {0 , 20, 30, 40 }
ac = { "a": 1, "b":2, "c":3 }

bb = tuple(aa)
bc = list(ac)
bd = dict({"a":ab[0], "b": ab[1],"C": ab[2],"d": ab[3],})


print(f"{aa[3][2]}" )
print(f"{bb}")
print(f"{bc}")
print(f"{bd}")



# print(aa)
# del aa[1]
# print(aa)
# del(aa[1])
# print(aa)