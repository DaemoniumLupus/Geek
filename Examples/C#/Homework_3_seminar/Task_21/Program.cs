double fx, fy, fz, sx, sy, sz;
double res;
try
{
  Console.Write("Введите x первой точки: ");
  fx = Convert.ToDouble(Console.ReadLine());
  Console.Write("Введите y первой точки: ");
  fy = Convert.ToDouble(Console.ReadLine());
  Console.Write("Введите z первой точки: ");
  fz = Convert.ToDouble(Console.ReadLine());
  Console.Write("Введите x второй точки: ");
  sx = Convert.ToDouble(Console.ReadLine());
  Console.Write("Введите y второй точки: ");
  sy = Convert.ToDouble(Console.ReadLine());
  Console.Write("Введите z второй точки: ");
  sz = Convert.ToDouble(Console.ReadLine());
}
catch (Exception exc)
{
  Console.WriteLine($"Ошибка ввода данных{exc.Message}");
  return;
}

res = Math.Sqrt(Math.Pow(sx - fx, 2) + Math.Pow(sy - fy, 2) + Math.Pow(sz - fz, 2));

Console.WriteLine($"A{{{fx},{fy},{fz}}}; B{{{sx},{sy},{sz}}} -> {res:f2}");

