Console.Clear();
Console.Write("Введите первое целое число-");
string input_1 = Console.ReadLine() ?? "";
int userNum = int.Parse(input_1);

switch (userNum)
{
  case 1:
    Console.WriteLine("Понедельник");
    break;
  case 2:
    Console.WriteLine("Вторник");
    break;
  case 3:
    Console.WriteLine("Среда");
    break;
  case 4:
    Console.WriteLine("Четверг");
    break;
  case 5:
    Console.WriteLine("Пятница");
    break;
  case 6:
    Console.WriteLine("Суббота");
    break;
  case 7:
    Console.WriteLine("Воскресенье");
    break;
  default:
    Console.WriteLine("Такого дня недели нет...");
    break;
}

