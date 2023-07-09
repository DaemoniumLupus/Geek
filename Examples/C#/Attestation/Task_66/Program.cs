int m = GetNumberFromUser("Введите значение числа M: ", "Ошибка ввода!");
int n = GetNumberFromUser("Введите значение числа N: ", "Ошибка ввода!");

if (n < m)
{
  int b = m;
  m = n;
  n = b;
}
int bufM = m;
int sum = 0;
SumNumber(m, n, sum, bufM);




void SumNumber(int m, int n, int sum, int bufM)
{
  if (m == n)
  {
    sum += m;
    Console.WriteLine($"M = {bufM}, N = {n} -> {sum}");
    return;
  }
  else
  {
    sum += m;
    SumNumber(m + 1, n, sum, bufM);
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