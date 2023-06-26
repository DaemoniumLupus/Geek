System.Threading.Thread.CurrentThread.CurrentCulture = new System.Globalization.CultureInfo("en-US");
Console.Clear();
int a = GetNumberFromUser("Введите количество чисел в массиве: ", "Ошибка ввода!");

double[] mas = new double[a];

GetArray(mas);
double max = NumberInArray(mas);
double min = NumberInArray(mas, "min");

double res = max - min;

WriteRes(mas, res,min,max);

double NumberInArray(double[] mas, string str = "max")
{
  double num = mas[0];
  for (int i = 1; i < mas.Length; i++)
  {
    if (str == "min")
    {
      if (mas[i] < num)
      {
        num = mas[i];
      }
    }
    else
    {
      if (mas[i] > num)
      {
        num = mas[i];
      }
    }

  }

  return num;
}

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

void GetArray(double[] arr)
{
  for (int i = 0; i < arr.Length; i++)
  {
    arr[i] = new Random().Next(0, 100);
    arr[i] += new Random().NextDouble();
  }
}

void WriteRes(double[] mas, double res,double min,double max)
{
  Console.Write("[");
  for (int i = 0; i < mas.Length; i++)
  {
    if (i + 1 == mas.Length)
    {
      Console.Write($"{mas[i]:f2}]");
    }
    else
    {
      Console.Write($"{mas[i]:f2}, ");
    }
  }
  Console.Write($" => {max:f2} - {min:f2} = {res:f2}");
}
