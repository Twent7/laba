using System;
using System.Collections.Generic;

namespace ToDoListApp
{
    class Program
    {
        static List<string> tasks = new List<string>();

        static void Main(string[] args)
        {
            while (true)
            {
                Console.WriteLine("Выберите действие: 1 - Добавить задачу, 2 - Удалить задачу, 3 - Просмотреть задачи, 0 - Выход");
                string choice = Console.ReadLine();

                switch (choice)
                {
                    case "1":
                        AddTask();
                        break;
                    case "2":
                        Console.WriteLine("Эта функция в разработке.");
                        break;
                    case "3":
                        ViewTasks();
                        break;
                    case "0":
                        return;
                    default:
                        Console.WriteLine("Некорректный ввод.");
                        break;
                }
            }
        }

        static void AddTask()
        {
            Console.WriteLine("Введите описание задачи:");
            string task = Console.ReadLine();
            tasks.Add(task);
            Console.WriteLine("Задача добавлена!");
        }

        static void ViewTasks()
        {
            Console.WriteLine("Список задач:");
            if (tasks.Count == 0)
            {
                Console.WriteLine("Список пуст.");
            }
            else
            {
                for (int i = 0; i < tasks.Count; i++)
                {
                    Console.WriteLine($"{i + 1}. {tasks[i]}");
                }
            }
        }
    }
}
