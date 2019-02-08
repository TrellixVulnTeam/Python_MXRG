# 1
# 입력데이터 처리
fhand = open('romeo.txt')

# 2
# 소문자변경 > 단어분리 > 단어갯수 세리기
counts = dict()
for line in fhand:
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# 3
# 리스트를 생성하지 않고 가장 많이 나온 단어 10개 출력
for key, val in sorted(((v, k) for k, v in counts.items()), reverse=True)[:10]:
    print(key, val)