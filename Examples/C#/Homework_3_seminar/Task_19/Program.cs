int num;
int fNum, lNum;
int fSnum, lSnum;

while (true)
{
  try
  {
    Console.Write("Введите пятизначное число: ");
    num = Convert.ToInt32(Console.ReadLine());
    if (num < 10000 || num > 99999)
    {
      Console.WriteLine("Ваше число не пятизначное!");
      continue;
    }
  }
  catch (Exception exc)
  {
    Console.WriteLine($"Ошибка типа данных {exc.Message}");
    return;
  }
  break;
}

fNum = num / 10000;
lNum = num % 10;

if (fNum != lNum)
{
  Console.WriteLine($"{num} -> Нет");
}
else
{
  fSnum = num / 1000;
  fSnum %= 10;

  lSnum = num % 100;
  lSnum /= 10;

  if (lSnum == fSnum)
  {
    Console.WriteLine($"{num} -> Да");
  }
  else
  {
    Console.WriteLine($"{num} -> Нет");
  }
}




