
bool[] mas = new bool[7];
for (int i = 0; i < 7; i++)
{
  if (i > 4)
  {
    mas[i] = true;
  }
  else
  {
    mas[i] = false;
  }
}
Console.Write("Enter the number of the day of the week: ");
int num = Convert.ToInt32(Console.ReadLine());
if (num < 1 || num > 7)
{
  Console.WriteLine($"There is no such day of the week {num}");
}
else
{
  if (mas[num-1])
  {
    Console.WriteLine("Yes");
  }
  else
  {
    Console.WriteLine("No");
  }
}
