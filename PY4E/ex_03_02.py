#try_except : 문자열이 들어갔을때 오류 처리하기

sh = input("enter hours : ")
sr = input("enter rate : ")

try :
    # 시급
    fr = float(sr)
    fh = float(sh)  #error발샐
except:
    print("Error, please enter numeric input")
    quit() # 뒷부분은 실행하지 않음

print(fh,fr)

if fh > 40 :
    reg = fr * fh
    #초과 금액 계산
    otp = (fh -40.0)*(fr*1.5)
    xp = reg + otp
else :
    xp = fr * fh

print("pay:", xp)


