int a, b, c;

Console.Write("Input first number: ");
a = Convert.ToInt32(Console.ReadLine());
Console.Write("Input second number: ");
b = Convert.ToInt32(Console.ReadLine());
Console.Write("Input third number: ");
c = Convert.ToInt32(Console.ReadLine());

if (a > b)
{
  Console.WriteLine($"max = {a}");
}
else if (b > c)
{
  Console.WriteLine($"max = {b}");
}
else
{
  Console.WriteLine($"max = {c}");
}

