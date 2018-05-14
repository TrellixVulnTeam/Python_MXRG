#1. 근무시간(hour), 시급(rate)가 인자인 함수(computepay)를 정의합니다.
def computepay(hours, rate) :
    #1-1. 근무시간이 40시간이 넘을 경우 시급의 1.5배를 계산한다.
    if fh > 40:
        reg = rate * hours
        # 초과 금액 계산
        otp = (hours - 40.0) * (rate * 1.5)
        pay = reg + otp
    #1-2. 근무시간이 40시간이 안넘을 경우 근무시간*시급을 계산합니다.
    else:
        pay = rate * hours

    #1-3. 계산된 급여를 반환합니다.
    return pay

#2. 근무시간(hour), 시급(rate) 입력받습니다.
sh = input("enter hours : ")
sr = input("enter rate : ")

try :
    # 2-1. 입력값이 숫자일 경우 float 형태로 변환합니다.
    fr = float(sr)
    fh = float(sh)
except:
    #2-2. 입력값이 문자일 경우 에러메시지를 출력하고 실행을 중단합니다.
    print("Error, please enter numeric input")
    quit()

#3. computepay( )함수를 호출합니다.
xp = computepay(fh,fr)

#4. 함수의 반환값을 출력합니다.
print("Pay:", xp)


