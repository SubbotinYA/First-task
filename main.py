# 1st program
#Выведите на экран(в консоль) результат: возведение числа 9 в степень 0.5, после умножение на 5
print(9**0.5*5)

# 2nd program
#Убедитесь в том что 9.99 больше 9.98 и 1000 не равно 1000.1 одновременно,
# выведете результат на экран(в консоль)
print(9.99 > 9.98 and 1000 != 1000.1)

# 3rd program
#Выведите на экран(в консоль) 2 умноженное на 2 плюс 2 без приоритета.
#Выведите на экран(в консоль) 2 умноженное на 2 плюс 2 с приоритетом для сложения.
#Выведите на экран(в консоль) результат сравнения этих двух выражений.
a = 2*2+2
print(a)
b = 2*(2+2)
print(b)
print(a == b)

#4th program
#Напишите в начале программы однострочный комментарий: "4th program".
#Дана строка '123.456'.
#Вывести на экран первую цифру после запятой - 4.
text = '123.456'
a=float(text) #преобразование из str в float
print (int(((a%1)*10))//1) #Оставляеи се цифры по сле точки, умножаем на 10, оставляем целое число, преобразуем полученное число в int