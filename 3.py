def intersection(lst,lst1):
    array=[]
    for element in lst:
        if element in lst1:
            array.append(element)
    return array
import random
while True:                                        #Проверка на дурака
    try:
        count = ( int(input('Введите колличество элементов первого массива:' )))
        count1 = ( int(input('Введите колличество элементов второго массива:' )))                                    
        break
    except ValueError:
         print('Вы должны ввести числа! Попробуйте снова!')
lst = [random.randint(0, 1000) for i in range(count)]
lst1 = [random.randint(0, 1000) for i in range(count1)]
print('Массив1:', lst)
print('Массив2:',lst1)
print('Общие элементы массивов:', intersection(lst,lst1))