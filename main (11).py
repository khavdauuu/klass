# задача 1
print("Задача 1")
def schet ():
    a = input("Введите первое число: ")
    a = float(a)
    b = input("Введите второе число: ")
    b = float(b)
    c = input("Введите третье число: ")
    c = float(c)
    if a > b:
        print(a-b)
    else: 
        print(b-a)
    return a, b
    if a > c:
        print(a-c)
    else:
        print(c-a)
    return a, c
    
c, d = schet()
e, f = schet()
z, x = schet()

#задача 2
print("задача 2")
def schet2 ():
    a = input("Введите первое число: ")
    a = float(a)
    b = input("Введите второе число: ")
    b = float(b)
    c = input("Введите третье число: ")
    c = float(c)
    if a > b:
        print(a-b)
    else: 
        print(b-a)
    return a, b
    if a > c:
        print(a+c)
    else:
        print(c+a)
    return a, c
    
c, d = schet2()
e, f = schet2()
z, x = schet2()

#задача 3
print("задача 3")
def schet3 ():
    a = input("Электричка едет со скоростью 70 км/час. В какую сторону летит дым? Ответ: ")
    b = input("Что принадлежит вам, но другие используют его чаще? Ответ: ")
    c = input("Каких камней нет ни в одном море? Ответ:  ")
    if a == "У электрички нет дыма":
        print("Вы угадали!")
    else:
        print("Неверно")
    return a
    if b == "Имя":
        print("Вы угадали!")
    elif b == "Ваше имя":
        print("Вы угадали!")
    else:
        print("Неверно")
    return b 
    if c == "Сухих":
        print("Вы угадали!")
    else:
        print("Неверно")
        
c, d = schet3()
e, f = schet3()
z, x = schet3()
    