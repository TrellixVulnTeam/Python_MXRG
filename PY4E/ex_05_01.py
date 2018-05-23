# 합계, 갯수, 평균, 예외처리하기 > done입력시 종료
num = 0
tot =0.0
while True :
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    # print(fval)
    num = num + 1  # count
    tot = tot + fval # 합계

# print('ALL Done')
print(tot, num, tot/num)