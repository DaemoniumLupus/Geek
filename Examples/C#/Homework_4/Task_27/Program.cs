using System;
Console.Clear();
int num = GetNumberFromUser("Ведите число: ", "Ошибка ввода!");
int bufNum = num;
int res = 0;

while(num > 0)
{
  res += num % 10;
  num /= 10;
}
Console.WriteLine($"{bufNum} -> {res}");




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