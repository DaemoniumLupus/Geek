

int[,] mas1 = new int[4, 4];
int[,] mas2 = new int[4, 4];
int[,] multiMas = new int[mas1.GetLength(0), mas2.GetLength(1)];

if (mas1.GetLength(0) == mas2.GetLength(1))
{
  mas1 = GetArray(mas1);
  mas2 = GetArray(mas2);

  multiMas = MultiplicatorMatrix(mas1, mas2, multiMas);

  PrintArray(mas1);
  PrintArray(mas2);
  PrintArray(multiMas);
}
else
{
  Console.WriteLine("Нельзя перемножить матрицы");
}




int[,] MultiplicatorMatrix(int[,] mas1, int[,] mas2, int[,] multiMas)
{
  for (int i = 0; i < multiMas.GetLength(0); i++)
  {
    for (int j = 0; j < multiMas.GetLength(1); j++)
    {
      multiMas[i, j] = MultiplicateElementMatrix(mas1, mas2, i, j);

    }
  }

  return multiMas;
}

int MultiplicateElementMatrix(int[,] mas1, int[,] mas2, int str, int column)
{
  int sum = 0;
  for (int i = 0; i < mas1.GetLength(0); i++)
  {
    sum += mas1[str, i] * mas2[i, column];
  }


  return sum;
}

int[,] GetArray(int[,] arr)
{
  for (int i = 0; i < arr.GetLength(0); i++)
  {
    for (int j = 0; j < arr.GetLength(1); j++)
    {
      arr[i, j] = new Random().Next(1, 6);
    }
  }
  return arr;
}

void PrintArray(int[,] arr)
{
  for (int i = 0; i < arr.GetLength(0); i++)
  {

    for (int j = 0; j < arr.GetLength(1); j++)
    {
      Console.Write(String.Format("{0,3}", arr[i, j]), " ");

    }
    Console.Write("\n");
  }
  Console.Write("\n");
}