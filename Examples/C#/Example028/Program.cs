Console.Clear();
int A = GetNumberFromUser("Введите целое число: ", "Ошибка ввода!");
int res = Multiplication(A);
Console.WriteLine($"{A} -> {res}");


int Multiplication(int num)
{
  int res = 1;
  while(num > 0)
  {
    res *= num;
    num--;
  }
  return res;
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