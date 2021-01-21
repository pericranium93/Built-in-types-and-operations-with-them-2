head_list = [8, 6, 6, 5, 2, 2, 1]
digit = int(input('Введите число'))
length = len(head_list)
for i in range(length):
    if digit > head_list[i]:
        head_list.insert(i, digit)
        break
    elif digit == head_list[i]:
        index = i
        while index != length:
            if index == length - 1:
                head_list.append(digit)
                break
            elif digit > head_list[index + 1]:
                index += 1
                head_list.insert(index, digit)
                break
            else:
                index += 1
        break
    else:
        continue
print('Окончательный рейтинг', head_list)



