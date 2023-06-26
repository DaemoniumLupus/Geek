Console.Clear();
int a = GetNumberFromUser("Введите количество чисел в массиве: ", "Ошибка ввода!");

int[] mas = new int[a];

GetArray(mas);

int res = SumOddNumbers(mas);

WriteRes(mas, res);






int SumOddNumbers(int[] mas)
{
  int sum = 0;

  for (int i = 1; i < mas.Length;i += 2)
  {
    sum += mas[i];
  }

    return sum;
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

void GetArray(int[] arr)
{
  for (int i = 0; i < arr.Length; i++)
  {
    arr[i] = new Random().Next(-1000, 1000);
  }
}

void WriteRes(int[] mas, int res)
{
  Console.Write("[");
  for (int i = 0; i < mas.Length; i++)
  {
    if (i + 1 == mas.Length)
    {
      Console.Write($"{mas[i]}]");
    }
    else
    {
      Console.Write($"{mas[i]}, ");
    }
  }
  Console.Write($" -> {res}");
}