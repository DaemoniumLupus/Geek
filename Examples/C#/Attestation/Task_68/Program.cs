ulong m = GetNumberFromUser("Введите число M: ", "Ошибка ввода!");
ulong n = GetNumberFromUser("Введите число N: ", "Ошибка ввода!");
 
Console.WriteLine( Akerman(m, n));








ulong Akerman(ulong m,ulong n)
{
if (m == 0) return n + 1;
else if (n == 0) return Akerman(m - 1, 1);
else return Akerman(m - 1, Akerman(m, n - 1));
}

ulong GetNumberFromUser(string message, string errorMessage)
{
  while (true)
  {
    Console.Write(message);
    if (ulong.TryParse(Console.ReadLine(), out ulong userNumber))
    {
      return userNumber;
    }
    Console.WriteLine(errorMessage);
  }
}