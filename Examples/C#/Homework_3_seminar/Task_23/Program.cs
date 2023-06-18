int num;
try
{
  Console.Write("Enter number: ");
  num = Convert.ToInt32(Console.ReadLine());
}
catch (Exception exc)
{
  Console.WriteLine($"Ошибка ввода данных{exc.Message}");
  return;
}

Console.Write($"{num} -> 1");
if (num > 1)
{
Console.Write(", ");
  for (int i = 2; i < num; i++)
  {
    Console.Write($"{Math.Pow(i, 3)}, ");
  }
Console.Write($"{Math.Pow(num, 3)}");
}