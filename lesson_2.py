money = 0
if money:
    print(f"You have {money} on your bank account")
else:
    print("You have no money and no debts")

#result = None
#if result:
 #   print(result)
#else:
 #   print("Result is None, do something")

#user_name = input("Enter your name: ")

#if user_name:
 #   print(f"Hello {user_name}")
#else:
 #  print("Hi Anonym!")

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True
print(a is c)  # False

#if x >= 0:
   # if y >= 0:  # x > 0, y > 0
   #     print("Перша чверть")
   # else:  # x > 0, y < 0
   #     print("Четверта чверть")
#else:
 #   if y >= 0:  # x < 0, y > 0
 #       print("Друга чверть")
 #   else:  # x < 0, y < 0
#       print("Третя чверть")

fruit = "apple"

match fruit:
    case "apple":
        print("This is an apple.")
    case "banana":
        print("This is a banana.")
    case "orange":
        print("This is an orange.")
    case _:
        print("Unknown fruit.")

fruit = 'apple'
for char in fruit:
    print(char)

alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
    print(char, end=" ")

some_iterable = ["a", "b", "c"]

for i in some_iterable:
    print(i)

odd_numbers = [1, 3, 5, 7, 9]
for i in odd_numbers:
    print(i ** 2)

k = 0
while k < 10:
    k = k + 1
print(k)

a = 0
while a < 6:
    a = a + 1
    if not a % 2:
        continue
    print(a)

for i in range(5):
    print(i)

for i in range(2, 10):
    print(i)

for i in range(0, 10, 2):
    print(i)

some_list = ["apple", "banana", "cherry"]
for index, value in enumerate(some_list):
    print(index, value)

list1 = ["зелене", "стигла", "червоний"]
list2 = ["яблуко", "вишня", "томат"]
for number, letter in zip(list1, list2):
    print(number, letter)

numbers = {
    1: "one",
    2: "two",
    3: "three"
}
for key in numbers:
    print(key)

for key in numbers.keys():
    print(key)

for val in numbers.values():
    print(val)

for key, value in numbers.items():
    print(key, value)

val = 'a'
try:
    val = int(val)
except ValueError:
    print(f"val {val} is not a number")
else:
    print(val > 0)
finally:
    print("This will be printed anyway")

def print_max(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'дорівнює', b)
    else:
        print(b, 'максимально')

print_max(3, 4)  # пряма передача значень

x = 5
y = 7
print_max(x, y)  # передача змінних у якості аргументів

def say_hello():
		# тіло функції
    print('Привіт, Світ!')

# Кінець функції say_hello()

# виклик функції
say_hello()

# ще один виклик функції
say_hello()

def print_max(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'дорівнює', b)
    else:
        print(b, 'максимально')

print_max(3, 4)  # пряма передача значень

x = 5
y = 7
print_max(x, y)  # передача змінних у якості аргументів

x = 50

def func() -> None:
    x = 2
    print('Зміна локального x на', x)  # Зміна локального x на 2

func()
print('Глобальний x як і раніше', x)  # x як і раніше 50

def outer_func():
    enclosing_var = "Я змінна в функції, що охоплює"

    def inner_func():
        print("Всередині вкладеної функції:", enclosing_var)

    inner_func()

outer_func()

x = 50

def func():
    global x
    print('x дорівнює', x)  # x дорівнює 50
    x = 2
    print('Змінюємо глобальне значення x на', x)  # Змінюємо глобальне значення x на 2

func()
print('Значення x складає', x)# Значення x складає 2

def greet(name, message="Привіт"):
    print(f"{message}, {name}!")

def func(a, b=5, c=10):
    print('a дорівнює', a,', b дорівнює', b,', а c дорівнює', c)

# a дорівнює 3, b дорівнює 7, а c дорівнює 10
func(3, 7)

# a дорівнює 25, b дорівнює 5, а c дорівнює 24
func(25, c=24)

# a дорівнює 100, b дорівнює 5, а c дорівнює 50
func(c=50, a=100)

def say(message, times=1):
    print(message * times)

say('Привіт') 
say('Світ', 5)

def print_all_args(*args):
    for arg in args:
        print(arg)

print_all_args(1, 'hello', True)

def factorial(n):
    if n == 0: # базовий випадок
        return 1
    else:
        return n * factorial(n-1) # рекурсивний випадок

print(factorial(5)) # виведе 120

def fibonacci(n):
    if n <= 1: # базовий випадок
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) # рекурсивний випадок

print(fibonacci(10)) # виведе 55

def factorial(n):
    print("Виклик функції factorial з n = ", n)
    if n == 1:
        print("Базовий випадок, n = 1, повернення 1")
        return 1
    else:
        result = n * factorial(n-1)
        print("Повернення результату для n = ", n, ": ", result)
        return result

print(factorial(5))
