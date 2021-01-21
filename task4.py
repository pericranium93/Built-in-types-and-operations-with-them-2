user_string = input('Введите вашу строку')
words = user_string.split()
for ind, words in enumerate(words, 1):
    print(ind, words[:10])
