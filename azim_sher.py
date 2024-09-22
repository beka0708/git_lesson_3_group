
word = str(input("Введите слова: "))
x = len(word)
i = 0
x = x - 1
k = 0
while x - i >= i:
    if word[x - i] == word[i]:
        i += 1
    else:
        k = 1
        break
if k == 1:
    print(f"{word}: это не полиндром")
else:
    print(f"{word}: это полиндром")
word = str(input("Введите слова: "))
x = len(word)
i = 0
x = x - 1
k = 0
while x - i >= i:
    if word[x - i] == word[i]:
        i += 1
    else:
        k = 1
        break
if k == 1:
    print(f"{word}: это не полиндром")
else:
    print(f"{word}: это полиндром")