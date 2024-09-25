import string

def count_words(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return len(words)



input_text = "Салам алейкум!! Кандайсын?"
word_count = count_words(input_text)
print("Количество слов:", word_count)





