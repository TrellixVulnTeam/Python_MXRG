
#
# total = 0
# count = 0
#
# while True:
#
#     inp = input('Enter a number:')
#
#     if inp == 'done' : break
#
#     value = float(inp)
#
#     total = total + value
#
#     count = count + 1
#
# average = total/count
#
# print('Average:', average)


# numlist = list()
#
# while True:
#
#     inp = input('Enter a number:')
#
#     if inp == 'done' : break
#
#     value = float(inp)
#
#     numlist.append(value)
#
# average = sum(numlist)/len(numlist)
#
# print('Average:', average)



fhand = open('mbox-short.txt')

for line in fhand:
    # 1.개행문자 공백제거
    line = line.rstrip()

    # 2.From 으로 시작하는 문장가져오기
    if not line.startswith('From ') : continue
    # 3.가져온 문장에서 요일부분 추출
    words = line.split()
    print(words[2])

    # 4.메일호스트 추출하기
    email = words[1]
    pieces = email.split('@')
    print(pieces[1])

