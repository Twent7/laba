class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class List:
    def __init__(self):
        self.items = []

    def append(self, value):
        """Добавляет элемент в конец списка."""
        self.items.append(value)

    def insert_at(self, index, value):
        """Вставляет элемент по указанному индексу."""
        if 0 <= index <= len(self.items):
            self.items.insert(index, value)
        else:
            raise IndexError("Индекс вне диапазона!")

    def remove_at(self, index):
        """Удаляет элемент по указанному индексу."""
        if 0 <= index < len(self.items):
            return self.items.pop(index)
        else:
            raise IndexError("Индекс вне диапазона!")

    def get(self, index):
        """Возвращает элемент по указанному индексу."""
        if 0 <= index < len(self.items):
            return self.items[index]
        else:
            raise IndexError("Индекс вне диапазона!")

    def is_empty(self):
        """Проверяет, пуст ли список."""
        return len(self.items) == 0


class Queue1:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        """Добавляет элемент в очередь."""
        self.items.append(value)

    def dequeue(self):
        """Удаляет элемент из очереди (FIFO)."""
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Очередь пуста!")

    def peek(self):
        """Возвращает первый элемент очереди, не удаляя его."""
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Очередь пуста!")

    def is_empty(self):
        """Проверяет, пуста ли очередь."""
        return len(self.items) == 0
    
class Queue2(List): #наследование
    def enqueue(self, value):
        """Добавляет элемент в конец очереди."""
        self.append(value)

    def dequeue(self):
        """Удаляет элемент из начала очереди."""
        if self.is_empty():
            raise IndexError("Очередь пуста.")
        return self.remove_at(0)

    def peek(self):
        """Возвращает первый элемент без удаления."""
        if self.is_empty():
            raise IndexError("Очередь пуста.")
        return self.get(0)


class Menu:
    def __init__(self):
        self.items = ["Выход"]
        self.item_methods = [self.quit]

    def add_menu_item(self, item_name, method):
        """Добавляет новый пункт меню."""
        self.items.insert(-1, item_name)
        self.item_methods.insert(-1, method)
        return len(self.items) - 2  # Возвращает индекс добавленного пункта

    def display(self):
        """Отображает меню."""
        print("\nМеню:")
        for i, item in enumerate(self.items, start=1):
            if item == "Выход":
                print(f"0. {item}")
            else:
                print(f"{i}. {item}")

    def process_menu(self):
        """Обрабатывает выбор пользователя."""
        while True:
            self.display()
            try:
                choice = int(input("Введите номер действия: "))
                if choice == 0:
                    self.quit()  # Теперь вызывается метод quit
                    break
                elif 1 <= choice < len(self.item_methods) + 1:
                    self.item_methods[choice - 1]()
                else:
                    print("Неверный выбор!")
            except ValueError:
                print("Введите корректное число!")

    def quit(self):
        """Метод для выхода из меню и перехода к следующему меню."""
        return


class ListMenu(Menu):
    def __init__(self):
        super().__init__()
        self.list = List()
        self.add_menu_item("Добавить элемент в конец", self.add_to_end)
        self.add_menu_item("Вставить элемент по индексу", self.insert_at_index)
        self.add_menu_item("Удалить элемент по индексу", self.remove_at_index)
        self.add_menu_item("Получить элемент по индексу", self.get_by_index)

    def add_to_end(self):
        value = int(input("Введите целое значение для добавления: "))
        self.list.append(value)
        print("Элемент добавлен в конец списка.")

    def insert_at_index(self):
        value = int(input("Введите целое значение для вставки: "))
        index = int(input("Введите индекс: "))
        try:
            self.list.insert_at(index, value)
            print("Элемент вставлен.")
        except IndexError as e:
            print(e)

    def remove_at_index(self):
        index = int(input("Введите индекс для удаления: "))
        try:
            value = self.list.remove_at(index)
            print(f"Элемент {value} удален.")
        except IndexError as e:
            print(e)

    def get_by_index(self):
        index = int(input("Введите индекс: "))
        try:
            value = self.list.get(index)
            print(f"Элемент на индексе {index}: {value}")
        except IndexError as e:
            print(e)


class QueueMenu(Menu):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue
        self.add_menu_item("Добавить элемент в очередь", self.enqueue)
        self.add_menu_item("Удалить элемент из очереди", self.dequeue)
        self.add_menu_item("Посмотреть первый элемент", self.peek)

    def enqueue(self):
        value = int(input("Введите целое значение для добавления в очередь: "))
        self.queue.enqueue(value)
        print("Элемент добавлен в очередь.")

    def dequeue(self):
        try:
            value = self.queue.dequeue()
            print(f"Элемент {value} удален из очереди.")
        except IndexError as e:
            print(e)

    def peek(self):
        try:
            value = self.queue.peek()
            print(f"Первый элемент очереди: {value}")
        except IndexError as e:
            print(e)


if __name__ == "__main__":
    print("Меню списка:")
    list_menu = ListMenu()
    list_menu.process_menu()  # После выхода из этого меню будет вызвано следующее

    print("\nМеню очереди (на основе List):")
    queue1_menu = QueueMenu(Queue1())
    queue1_menu.process_menu()  # После выхода из этого меню будет завершение программы

    print("\nМеню очереди (с наследованием от List):")
    queue2_menu = QueueMenu(Queue2())
    queue2_menu.process_menu()
