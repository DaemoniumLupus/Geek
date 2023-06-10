
int a, b;

Console.Write("Input first number: ");
a = Convert.ToInt32(Console.ReadLine());
Console.Write("Input second number: ");
b = Convert.ToInt32(Console.ReadLine());

if (a > b)
{
  Console.WriteLine($"max = {a}");
}
else
{
  Console.WriteLine($"max = {b}");
}