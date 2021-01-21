
user_list = list(input('Введите элементы списка'))
length = len(user_list)
print('Вы создали список', user_list)
num = 0
for i in range(length // 2):
    element = user_list.pop(num)
    user_list.insert(num + 1, element)
    num += 2
print('Получился список', user_list)

