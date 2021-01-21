quantity_of_position = int(input('Сколько товарных позиций вы будете вносить?'))
i = 1
comp_list = []
product_tup = ()
product_list = []
prd, prc, quan, unt = [], [], [], []
analyst = {'Название': prd, 'Цена': prc, 'Количество': quan, 'Ед.': unt}

while i != quantity_of_position + 1:
    number = i
    product = input('Введите название товара или наберите "q" для прекращения ввода')
    if product == 'q':
        break
    price = float(input('Введите цену товара за единицу'))
    quantity_of_product = int(input('Введите количество товара'))
    unit = input('Введите единицу измерения')
    prd.append(product)
    prc.append(price)
    quan.append(quantity_of_product)
    unt.append(unit)
    product_dict = {'Название': product, 'Цена': price, 'Количество': quantity_of_product, 'Ед.': unit}
    comp_list.append(i)
    comp_list.append(product_dict)
    product_tup = tuple(comp_list)
    product_list.append(product_tup)
    comp_list = []
    i += 1

print(product_list)
print(analyst)

# print(product_list[0][1].get('Название'))
