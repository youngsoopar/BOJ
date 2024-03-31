alpha = [0 for _ in range(26)]
text = input()

for i in text:
    alpha[ord(i)-ord('a')]+=1
    
print(*alpha) # *는 unpacking. 리스트에서 꺼내옴.