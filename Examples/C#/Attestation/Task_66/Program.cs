int m = GetNumberFromUser("Введите значение числа M: ", "Ошибка ввода!");
int n = GetNumberFromUser("Введите значение числа N: ", "Ошибка ввода!");

if (n < m)
{
  int b = m;
  m = n;
  n = b;
}
int buf = m;
int sum = 0;
SumNumber(m, n, sum, buf);




void SumNumber(int m, int n, int sum, int buf)
{
  if (m == n)
  {
    sum += m;
    Console.WriteLine($"M = {buf}, N = {n} -> {sum}");
    return;
  }
  else
  {
    sum += m;
    SumNumber(m + 1, n, sum, buf);
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