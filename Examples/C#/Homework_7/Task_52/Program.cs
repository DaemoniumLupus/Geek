int[,] arr = new int[10, 10];
arr = GetArray(arr);

PrintArray(arr);

double[] average = new double[10];

Calculation(arr, average);

PrintRes(average);



void Calculation(int[,] arr, double[] average)
{
  int sizeOfColumn = arr.GetLength(0);
  for (int j = 0; j < arr.GetLength(1); j++)
  {
    for (int i = 0; i < arr.GetLength(0); i++)
    {
      average[j] += arr[i, j];
    }
    average[j] /= arr.GetLength(0);
  }
}


int[,] GetArray(int[,] arr)
{
  for (int i = 0; i < arr.GetLength(0); i++)
  {
    for (int j = 0; j < arr.GetLength(1); j++)
    {
      arr[i, j] = new Random().Next(0, 100);
    }
  }
  return arr;
}

void PrintArray(int[,] arr)
{
  for (int i = 0; i < arr.GetLength(0); i++)
  {
    //Console.WriteLine(string.Join(" ", arr[i]));
    for (int j = 0; j < arr.GetLength(1); j++)
    {
      Console.Write(String.Format("{0,3}", arr[i, j]), " ");

    }
    Console.Write("\n");
  }
  Console.Write("\n");
}

void PrintRes(double[] average)
{
  Console.WriteLine("Среднее арифметическое каждого столбца: ");
  for (int i = 0; i < arr.GetLength(1); i++)
  {
    Console.Write(String.Format("{0,5:f1}", average[i]), " ");
  }
}
