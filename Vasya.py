speed = float(input("Средняя скорость: "))
time = int(input("Верям в пути: "))

point = time * speed # Вычисляем точку остановки
if point > 100:
    print("поехал по второму кругу, пройденное растояние = ", point)
elif point < 0:
    print("велосипедист едет назад уже", point , "километров")
elif point == 0:
    print("Велосипедист ни куда не едет, скорость = " , speed)
else:
 print("Велосипидист на ", point, )  # Выводим итог

input("Нажмите Enter для выхода") # Просим нажать кнопку для завершения программы