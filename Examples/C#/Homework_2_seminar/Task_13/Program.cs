
int Transform(int num)
{
  while (num > 999)
  {
    num /= 10;
  }
  return num;
}
void Result(int num)
{
  Console.WriteLine(num % 10);
}


Console.WriteLine("Enter number: ");
int num = Convert.ToInt32(Console.ReadLine());
if (num < 100)
{
  Console.WriteLine($"{num} -> Третьей цифры нет");
}
else if (num > 999)
{
  num = Transform(num);
  Result(num);
}
else
{
  Result(num);
}




