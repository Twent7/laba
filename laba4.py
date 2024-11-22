class Test:
    def __init__(self, w=1):
        self._W = w  # Защищенное поле W

    def _Z(self):
        print("Это закрытая функция класса Test")


# Функция-друг, которая может обращаться к защищенным элементам класса Test
def fun(t):
    print("Значение параметра W:", t._W)
    t._Z()  # Вызов защищенной функции


class B:
    def __init__(self):
        self.__secret = 42  # Приватное поле

class A:
    def access_b_secret(self, b):
        # Доступ к приватному полю класса B
        print("Доступ к закрытому полю класса B:", b._B__secret)


class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        return f"{self.real}{'+' if self.imag >= 0 else ''}{self.imag}i"

    @staticmethod
    def from_input():
        real = float(input("Введите действительную часть: "))
        imag = float(input("Введите мнимую часть: "))
        return Complex(real, imag)


class Array:
    def __init__(self):
        self.data = []

    def add(self, value):
        """Добавление элемента в массив"""
        self.data.append(value)

    def remove(self, index):
        """Удаление элемента по индексу"""
        if 0 <= index < len(self.data):
            self.data.pop(index)
        else:
            print("Ошибка: неверный индекс!")

    def __getitem__(self, index):
        """Перегрузка оператора индексирования"""
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            raise IndexError("Неверный индекс")

    def __str__(self):
        """Отображение элементов массива"""
        return " ".join(str(val) for val in self.data)


if __name__ == "__main__":
    # Работа с классом Test и функцией fun
    print("=== Test и fun ===")
    t = Test()
    fun(t)

    # Работа с классами A и B
    print("\n=== A и B ===")
    a = A()
    b = B()
    a.access_b_secret(b)

    # Работа с классом Complex
    print("\n=== Complex ===")
    c1 = Complex(1, 2)
    c2 = Complex(3, 4)
    print("Сумма:", c1 + c2)
    print("Разность:", c1 - c2)

    # Работа с классом Array
    print("\n=== Array ===")
    arr = Array()
    arr.add(10)
    arr.add(20)
    arr.add(30)
    print("Массив:", arr)

    arr.remove(1)
    print("После удаления:", arr)

    try:
        print("Элемент по индексу 1:", arr[1])
    except IndexError as e:
        print(e)
