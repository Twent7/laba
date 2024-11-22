class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remove(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("Пусто")

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" <- ")
            current = current.prev
        print("Пусто")

class Menu:
    def __init__(self, options):
        self.options = options

    def display(self):
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")
        print("0. Выход")

    def get_choice(self):
        try:
            return int(input("Введите ваш выбор: "))
        except ValueError:
            return -1

class ListMenu:
    def __init__(self):
        self.list = List()

    def run(self):
        menu = Menu(["Добавить элемент", "Удалить элемент", "Вывести список вперед", "Вывести список назад"])
        while True:
            menu.display()
            choice = menu.get_choice()
            if choice == 0:
                break
            elif choice == 1:
                data = input("Введите элемент для добавления: ")
                self.list.append(data)
            elif choice == 2:
                data = input("Введите элемент для удаления: ")
                self.list.remove(data)
            elif choice == 3:
                self.list.display_forward()
            elif choice == 4:
                self.list.display_backward()
            else:
                print("Неверный выбор!")

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print("Стек пуст!")
            return None
        return self.items.pop()

    def top(self):
        if self.is_empty():
            print("Стек пуст!")
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

class StackMenu:
    def __init__(self):
        self.stack = Stack()

    def run(self):
        menu = Menu(["Добавить элемент в стек", "Удалить элемент из стека", "Посмотреть верхний элемент", "Проверить, пуст ли стек"])
        while True:
            menu.display()
            choice = menu.get_choice()
            if choice == 0:
                break
            elif choice == 1:
                item = input("Введите элемент для добавления: ")
                self.stack.push(item)
            elif choice == 2:
                print(f"Удаленный элемент: {self.stack.pop()}")
            elif choice == 3:
                print(f"Верхний элемент: {self.stack.top()}")
            elif choice == 4:
                print("Стек пуст!" if self.stack.is_empty() else "Стек не пуст.")
            else:
                print("Неверный выбор!")

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Очередь пуста!")
            return None
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            print("Очередь пуста!")
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

class QueueMenu:
    def __init__(self):
        self.queue = Queue()

    def run(self):
        menu = Menu(["Добавить элемент в очередь", "Удалить элемент из очереди", "Посмотреть первый элемент", "Проверить, пуста ли очередь"])
        while True:
            menu.display()
            choice = menu.get_choice()
            if choice == 0:
                break
            elif choice == 1:
                item = input("Введите элемент для добавления: ")
                self.queue.enqueue(item)
            elif choice == 2:
                print(f"Удаленный элемент: {self.queue.dequeue()}")
            elif choice == 3:
                print(f"Первый элемент: {self.queue.front()}")
            elif choice == 4:
                print("Очередь пуста!" if self.queue.is_empty() else "Очередь не пуста.")
            else:
                print("Неверный выбор!")

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)

    def find(self, value):
        return self._find(self.root, value)

    def _find(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._find(node.left, value)
        return self._find(node.right)

    def display(self):
        levels = []
        self._display(self.root, 0, levels)
        for level in levels:
            print(" ".join(str(node.value) if node else "-" for node in level))

    def _display(self, node, depth, levels):
        if len(levels) <= depth:
            levels.append([])
        levels[depth].append(node)
        if node:
            self._display(node.left, depth + 1, levels)
            self._display(node.right, depth + 1, levels)
class TreeMenu:
    def __init__(self):
        self.tree = BinarySearchTree()

    def run(self):
        menu = Menu(["Добавить элемент", "Найти элемент", "Вывести дерево"])
        while True:
            menu.display()
            choice = menu.get_choice()
            if choice == 0:
                break
            elif choice == 1:
                value = int(input("Введите значение для добавления: "))
                self.tree.insert(value)
                print(f"Значение {value} добавлено в дерево.")
            elif choice == 2:
                value = int(input("Введите значение для поиска: "))
                node = self.tree.find(value)
                if node:
                    print(f"Элемент {value} найден.")
                else:
                    print(f"Элемент {value} отсутствует.")
            elif choice == 3:
                print("Текущее состояние дерева:")
                self.tree.display()
            else:
                print("Неверный выбор!")

if __name__ == "__main__":
    print("\nМеню двунаправленного списка:")
    list_menu = ListMenu()
    list_menu.run()

    print("\nМеню стека:")
    stack_menu = StackMenu()
    stack_menu.run()

    print("\nМеню очереди:")
    queue_menu = QueueMenu()
    queue_menu.run()

    print("\nМеню двоичного дерева поиска:")
    tree_menu = TreeMenu()
    tree_menu.run()