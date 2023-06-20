
Console.Clear();
int A = GetNumberFromUser("Введите целое число: ", "Ошибка ввода!");
ulong res = Multiplication((ulong) A);
Console.WriteLine($"{A} -> {res}");


ulong Multiplication(ulong num)
{
  ulong res = 1;
  while(num > 0)
  {
    res = res * num;
   /*  Console.WriteLine(num); */
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