def is_palindrome(words):
    x = len(words)
    i = 0
    x = x - 1
    k = 0
    while x - i >= i:
        if words[x - i] == words[i]:
            i += 1
        else:
            k = 1
            break

    return k == 0


while True:
    word = input("Введите слово (или 'выход' для завершения): ")
    if word.lower() == 'выход':
        break
    if is_palindrome(word):
        print(f"{word}: это палиндром")
    else:
        print(f"{word}: это не палиндром")
