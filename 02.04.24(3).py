# задача 4
def schet ():
    is_year_leap = input("Напишите дней в году: ")
    if is_year_leap == '365':
        print("Год не високосный")
    elif is_year_leap == '366':
        print("Год високосный")
    else:
        print("Введите либо 365, либо 366")
    return is_year_leap
    
c, d = schet()
e, f = schet()
z, x = schet()
