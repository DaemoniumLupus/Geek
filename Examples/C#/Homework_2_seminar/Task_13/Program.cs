using System;
int Transform(int num)
{
  while (num > 999)
  {
    num /= 10;
  }
  return num;
}
int Result(int num){

}

int res;
Console.WriteLine("Enter number: ");
int num = Convert.ToInt32(Console.ReadLine());
if (num < 100)
{
  Console.WriteLine($"{num} -> Третьей цифры нет");
}
else if (num > 999)
{
  num = Transform(num);
  res = Result(num);
} else{
res = Result(num);
}
  



