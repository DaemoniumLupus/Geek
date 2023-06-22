Console.Clear();
int a = GetNumberFromUser("Введите число А: ", "Ошибка ввода!");
int b = GetNumberFromUser("Введите число В: ", "Ошибка ввода!");
int res = a;

for (int i = 1; i < b;i++)
{
res *= a;
}

Console.WriteLine($"{a},{b} -> {res}");

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