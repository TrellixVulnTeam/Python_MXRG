sh = input("enter hours : ")
sr = input("enter rate : ")
# 시급
fr = float(sr)
fh = float(sh)
# print(fh, fr)

if fh > 40 :
    print("overtime")
    reg = fr * fh
    #초과 금액 계산
    otp = (fh -40.0)*(fr*1.5)
    print(reg, otp)
    xp = reg + otp
else :
    print("regular")
    xp = fr * fh

print("pay:", xp)


