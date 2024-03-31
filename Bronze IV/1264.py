aeiou_list = ['a','e','i','o','u',"A","E","I","O","U"]

while True:
    sentence = str(input())
    if sentence == "#":
        break
    b = 0
    for i in range(len(aeiou_list)):
        c = sentence.count(aeiou_list[i])
        b +=c
    print(b)