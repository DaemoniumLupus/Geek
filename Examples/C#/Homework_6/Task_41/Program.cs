int size = GetNumberFromUser("Введите количество чисел: ", "Ошибка ввода!");
int[] mas = new int[size];
int res;

WriteMassive(mas);

res = NumbersOfPositive(mas);

WriteRes(mas, res);



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

int NumbersOfPositive(int[] mas)
{
  int count = 0;
  for (int i = 0; i < mas.Length; i++)
  {
    if (mas[i] > 0){
      count++;
    }
  }
  return count;
}

void WriteMassive(int[] mas)
{
  for (int i = 0; i < mas.Length; i++)
  {
    mas[i] = GetNumberFromUser($"Введите {i + 1}-е число: ", "Ошибка ввода!");
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