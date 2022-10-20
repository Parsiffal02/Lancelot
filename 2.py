import math 
def area_of_the_circle(Radius):  
    area = Radius** 2 * math.pi 
    return area
while True:                                        #Проверка на дурака
    try:
        Radius = float(input("Пожалуйста, введите радиус окружности: "))                              
        break
    except ValueError:
        print('Вы должны ввести число! Попробуйте снова!')
print(" Площадь окружности равна: ", area_of_the_circle(Radius))