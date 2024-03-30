word = input().upper()
word_list = list(set(word))
c = []

for i in word_list:
    d = word.count(i)
    c.append(d)

if c.count(max(c)) >= 2:
    print('?')
else:
    print(word_list[(c.index(max(c)))])