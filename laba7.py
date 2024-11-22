import numpy as np

# Задача 2: Шаблон функции Max и специализированная версия для строк
def max_value(x, y):
    print("Вызвана шаблонная функция Max.")
    return x if x > y else y

# Специализированная версия для строк
def max_value(x: str, y: str) -> str:
    print("Вызвана специализированная функция Max для строк.")
    return x if x > y else y

# Тестирование Max
x_num = 10
y_num = 20
print(f"Максимум среди чисел {x_num} и {y_num}: {max_value(x_num, y_num)}")

str1 = "Apple"
str2 = "Banana"
print(f"Максимум среди строк '{str1}' и '{str2}': {max_value(str1, str2)}")


# Задача 3: Шаблон функции для суммы аргументов (числа или массивы)

# Шаблонная функция для суммы
def sum_values(x, y):
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        return x + y
    elif isinstance(x, list) and isinstance(y, list):
        # Для массивов (списков)
        return x[0] + y[0] if len(x) > 0 and len(y) > 0 else 0
    else:
        print("Не арифметические типы и не массивы элементов арифметических типов.")
        return 0

# Примеры использования
print(f"Сумма чисел: {sum_values(10, 20)}")

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
print(f"Сумма массивов: {sum_values(arr1, arr2)}")

# Пример с неподходящими типами
print(f"Сумма строк: {sum_values('Hello', 'World')}")


# Задача 4: Шаблон класса для матриц с операциями сложения, вычитания и ввода/вывода

class Matrix:
    def __init__(self, rows, cols, values=None):
        self.rows = rows
        self.cols = cols
        self.mat = values if values else [[0] * cols for _ in range(rows)]

    def input_matrix(self):
        print(f"Введите элементы матрицы {self.rows}x{self.cols}:")
        for i in range(self.rows):
            for j in range(self.cols):
                self.mat[i][j] = int(input(f"Элемент [{i}][{j}]: "))

    def display_matrix(self):
        for row in self.mat:
            print(" ".join(map(str, row)))

    # Операция сложения
    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Размеры матриц должны совпадать для сложения.")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.mat[i][j] = self.mat[i][j] + other.mat[i][j]
        return result

    # Операция вычитания
    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Размеры матриц должны совпадать для вычитания.")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.mat[i][j] = self.mat[i][j] - other.mat[i][j]
        return result

# Тестирование матриц
matrix1 = Matrix(2, 2)
matrix1.input_matrix()
print("Матрица 1:")
matrix1.display_matrix()

matrix2 = Matrix(2, 2)
matrix2.input_matrix()
print("Матрица 2:")
matrix2.display_matrix()

sum_matrix = matrix1 + matrix2
print("Сумма матриц:")
sum_matrix.display_matrix()

diff_matrix = matrix1 - matrix2
print("Разность матриц:")
diff_matrix.display_matrix()


# Задача 5: Шаблон класса для текстового меню

class Menu:
    def __init__(self):
        self.items = []
        self.actions = []

    def add_item(self, item, action):
        self.items.append(item)
        self.actions.append(action)

    def display(self):
        print("Меню:")
        for i, item in enumerate(self.items):
            print(f"{i + 1}. {item}")

    def run(self):
        while True:
            self.display()
            choice = int(input("Введите номер действия: "))
            if 1 <= choice <= len(self.actions):
                self.actions[choice - 1]()
            else:
                print("Неверный выбор!")

# Функции для меню
def action1():
    print("Вы выбрали действие 1")

def action2():
    print("Вы выбрали действие 2")

# Тестирование меню
menu = Menu()
menu.add_item("Действие 1", action1)
menu.add_item("Действие 2", action2)
menu.run()
