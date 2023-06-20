

int A = GetNumberFromUser("Введите целое число A: ", "Ошибка ввода!");
int sumNumbers = GetSumNumbers(A);
Console.WriteLine($"{A} -> {sumNumbers}");


/////////////////////////////////////////////////////

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

int GetSumNumbers(int num)
{
  int sum = 0;
  while (num > 0)
  {
    sum += num;
    num--;
  }
  return sum;
}


