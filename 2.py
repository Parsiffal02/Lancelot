import math 
def area_of_the_circle(Radius):  
    area = Radius** 2 * math.pi 
    return area  
Radius = float(input("Пожалуйста, введите радиус окружности: ")) 
print(" Площадь окружности равна: ", area_of_the_circle(Radius))