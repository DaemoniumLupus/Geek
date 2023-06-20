int A = GetNumberFromUser("Введите целое число: ", "Ошибка ввода!");
int res;

res = GetCount(A);

Console.WriteLine(res);


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

int GetCount(int num)
{
  int count = 0;
  while (num > 0)
  {
    count++;
    num /= 10;
  }
  return count;
}