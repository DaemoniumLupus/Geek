System.Threading.Thread.CurrentThread.CurrentCulture
= new System.Globalization.CultureInfo("en-US"); int m, n;

m = GetNumberFromUser("m = ", "Ошибка ввода!");
n = GetNumberFromUser("n = ", "Ошибка ввода!");

double[,] doubleArray = new double[m, n];
doubleArray = GetDoubleArray(doubleArray, m, n);

PrintArray(doubleArray);


void PrintArray(double[,] arr)
{
  for (int i = 0; i < arr.GetLength(0); i++)
  {
    //Console.WriteLine(string.Join(" ", arr[i]));
    for (int j = 0; j < arr.GetLength(1); j++)
    {
      Console.Write(String.Format("{0,7:f2}", arr[i, j]), " ");

    }
    Console.Write("\n");
  }

}

double[,] GetDoubleArray(double[,] arr, int m, int n)
{
  for (int i = 0; i < arr.GetLength(0); i++)
  {
    for (int j = 0; j < arr.GetLength(1); j++)
    {
      arr[i, j] = new Random().Next(-100, 100);
      arr[i, j] += new Random().NextDouble();
    }
  }
  return arr;
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