Console.Clear();

int countArr = GetNumberFromUser("Введите количество элементов массива: ", "Ошибка ввода!");

int[] Arr = new int[countArr];

int min, max;
int command = 0;

min = GetNumberFromUser("Введите минимальное число элемента массива: ", "Ошибка ввода!");
max = GetNumberFromUser("Введите максимальное число элемента массива: ", "Ошибка ввода!");

ArrayRand(Arr, min, max);

Write(Arr);

while (true)
{
  
  command = GetNumberFromUser("\nВведите номер команды:\r\n(1)Показать элемент по расположению\r\n(2)Найти элемент и вывести его расположение\r\n(3)Вывод всего массива\r\n(4)Выход\n", "Ошибка ввода!");
  if (command == 1)
  {
    searchIndexNum(Arr);
  }
  else if (command == 2)
  {
    searchNum(Arr);
  }
  else if (command == 3)
  {
    Write(Arr);
  }
  else if (command == 4)
  {
    return;
  }
  else
  {
    Console.WriteLine("Incorrect command");
  }
}

void searchIndexNum(int[] mas)
{
  while (true)
  {
    int i = GetNumberFromUser($"Введите позицию числа от 1 до {mas.Length}: ", "Ошибка ввода!");
    if (i > mas.Length || i <= 0)
    {
      Console.WriteLine("Некоректное число!");
    }
    else
    {
      Console.WriteLine($"На позиции {i} находится число {mas[i - 1]}");
      return;
    }
  }
}


void searchNum(int[] mas)
{
  int[] indexMas = new int[1];
  int count = 0;

  int num = GetNumberFromUser("Введите искомое число: ", "Ошибка ввода!");
  
  for (int i = 0; i < mas.Length; i++)
  {
    if (num == mas[i])
    {
      count++;
    }
  }
  if (count > 0)
  {
    indexMas = new int[count];
    int j = 0;
    for (int i = 0; i < mas.Length; i++)
    {
      if (num == mas[i])
      {
        indexMas[j] = i;
        j++;
      }
    }
  }
  
  if (count == 1)
  {
    Console.WriteLine($"Ваше число ({num}) находится по индексу {indexMas[0]}");
  }
  else if (count == 0)
  {
    Console.WriteLine("Вашего числа нет в массиве!");
  }
  else
  {
    Console.Write($"Ваше число ({num}) находится по индексам {{");
    for (int i = 0; i < indexMas.Length;i++)
    {
      if (i + 1 == indexMas.Length)
      {
        Console.Write($"{indexMas[i]}}}");
      }else {
        Console.Write($"{indexMas[i]}, ");
      }
    }
  }

}

int GetNumberFromUser(string message, string errorMessage)
{
  while (true)
  {
    Console.Write(message);
    if (int.TryParse(Console.ReadLine(), out int userNumber))
    {
      return userNumber;
    }
    Console.WriteLine(errorMessage);
  }
}

void ArrayRand(int[] RandomArray, int a, int b)
{
  for (int i = 0; i < RandomArray.Length; i++)
  {
    RandomArray[i] = Rand(a, b);
  }

}


int Rand(int a, int b)
{
  return new Random().Next(a, b);
}

void Write(int[] RandomArray)
{
  Console.Write("{");

  for (int i = 0; i < RandomArray.Length; i++)
  {
    if (i + 1 == RandomArray.Length)
    {
      Console.Write($"{RandomArray[i]}");
    }
    else
    {
      Console.Write($"{RandomArray[i]}, ");
    }
  }

  Console.Write("}");
}