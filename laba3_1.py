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
        if self.head is None:  # если список пуст
            self.head = self.tail = new_node
        else:  # добавляем элемент в конец списка
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:  # если список пуст
            self.head = self.tail = new_node
        else:  # добавляем элемент в начало списка
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


class Menu:
    def __init__(self, list_obj):
        self.list_obj = list_obj

    def show_menu(self):
        while True:
            print("\n1. Добавить элемент в конец списка")
            print("2. Добавить элемент в начало списка")
            print("3. Удалить элемент из списка")
            print("4. Показать список")
            print("5. Выход")
            choice = input("Выберите действие: ")

            if choice == "1":
                data = input("Введите элемент для добавления в конец: ")
                self.list_obj.append(data)
            elif choice == "2":
                data = input("Введите элемент для добавления в начало: ")
                self.list_obj.prepend(data)
            elif choice == "3":
                data = input("Введите элемент для удаления: ")
                self.list_obj.delete(data)
            elif choice == "4":
                self.list_obj.display()
            elif choice == "5":
                break
            else:
                print("Неверный выбор. Попробуйте снова.")


# Реализация стека и очереди через агрегирование

class StackAggregated:
    def __init__(self):
        self.list = List()

    def push(self, data):
        self.list.append(data)

    def pop(self):
        if self.list.tail is None:
            return None
        data = self.list.tail.data
        self.list.delete(data)
        return data


class QueueAggregated:
    def __init__(self):
        self.list = List()

    def enqueue(self, data):
        self.list.append(data)

    def dequeue(self):
        if self.list.head is None:
            return None
        data = self.list.head.data
        self.list.delete(data)
        return data


# Реализация стека и очереди через наследование

class StackInherited(List):
    def push(self, data):
        self.append(data)

    def pop(self):
        if self.tail is None:
            return None
        data = self.tail.data
        self.delete(data)
        return data


class QueueInherited(List):
    def enqueue(self, data):
        self.append(data)

    def dequeue(self):
        if self.head is None:
            return None
        data = self.head.data
        self.delete(data)
        return data

if __name__ == "__main__":
    print("Тестирование двунаправленного списка с текстовым меню")
    my_list = List()
    menu = Menu(my_list)
    menu.show_menu()

    print("Тестирование стека и очереди через агрегирование")
    stack_agg = StackAggregated()
    queue_agg = QueueAggregated()

    stack_agg.push(10)
    stack_agg.push(20)
    print("Стек после добавления элементов (агрегирование):")
    stack_agg.list.display()

    print("Извлечение элемента из стека (агрегирование):", stack_agg.pop())
    stack_agg.list.display()

    queue_agg.enqueue(1)
    queue_agg.enqueue(2)
    print("Очередь после добавления элементов (агрегирование):")
    queue_agg.list.display()

    print("Извлечение элемента из очереди (агрегирование):", queue_agg.dequeue())
    queue_agg.list.display()

    print("\nТестирование стека и очереди через наследование")
    stack_inh = StackInherited()
    queue_inh = QueueInherited()

    stack_inh.push(30)
    stack_inh.push(40)
    print("Стек после добавления элементов (наследование):")
    stack_inh.display()

    print("Извлечение элемента из стека (наследование):", stack_inh.pop())
    stack_inh.display()

    queue_inh.enqueue(3)
    queue_inh.enqueue(4)
    print("Очередь после добавления элементов (наследование):")
    queue_inh.display()

    print("Извлечение элемента из очереди (наследование):", queue_inh.dequeue())
    queue_inh.display()
