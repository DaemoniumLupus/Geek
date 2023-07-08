int n = GetNumberFromUser("Введите целое число: ", "Ошибка ввода");
Console.Write($"N = {n} -> \"");
Recursion(n);
Console.Write("\"");

void Recursion(int n)
{
  if (n == 0)
  {
    return;
  }
  else
  {
    if (n == 1) Console.Write($"{n}"); 
    else Console.Write($"{n},");
    Recursion(n - 1);
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