#coding: utf-8
#Задание 1 
surname = input("Введите Фамилию: ")
country = input("Введите страну: ")
year = int(input("Ввведите год: "))
cost = float(input("Введите стоимость: "))

tourist_info = {
    "Фамилия": surname,
    "Страна": country,
    "Год": year,
    "Стоимость": cost
}

print("\nОбновлённая туристическая информация:")
print("Фамилия:", tourist_info["Фамилия"])
print("Страна:", tourist_info["Страна"])
print("Год:", tourist_info["Год"])
print("Стоимость:", tourist_info["Стоимость"])

#Задание 2 
A = int(input("Введите значение А: ")) #Вводим А
B = int(input("Введите значение B: ")) #Вводим В
C = int(input("Введите значение C: ")) #Вводим С
a = (A*(B/3.14)+(C*3+5)) #Выражаем это через новую переменную
print(a) #Выводим результат

#Задание 3 
R = int(input("Введите значение для R: ")); Y = int(input("Введите значение для Y: ")); print(R*Y**2+(Y/5)) #Введём две переменные #Выведем то, что у нас получилось

#Задание 4 
A = float(input("Введите положительное действительное число: "))
integer_part = int(A)
fractional_part = A - integer_part

root = A**0.5
remainder = A % 5

print("\nЦелочисленная часть:", integer_part)
print("Дробная часть:", fractional_part)
print("Арифметический квадратный корень:", root)
print("Остаток деления на 5:", remainder)

#Задание 5 
minutes = int(input("Введите количество минут: "))
hours = minutes // 60
remaining_minutes = minutes % 60

print("\nВремя в часах и минутах:")
print(hours, "Часов и", minutes, "Минут")