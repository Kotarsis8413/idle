print("1:калькулятор\n2:калькулятор степеней")


vibor = int(input("вибирите действие~~~~~>"))

if (vibor==1):
    while True: print(eval(input("~~~>")))
if (vibor==2):
    while True:
            chislo = int(input("введите число"))
            stepen = int(input("введите степень"))
            otvet = chislo ** stepen
            print(otvet)
