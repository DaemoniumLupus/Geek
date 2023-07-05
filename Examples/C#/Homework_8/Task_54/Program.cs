int[,] arr = new int[10, 10];
int[] bufSringArr = new int[arr.GetLength(1)];

arr = GetArray(arr);

PrintArray(arr);

for (int i = 0; i < arr.GetLength(0); i++)
{
  bufSringArr = GetStringArray(arr, i);
  SortArr(bufSringArr);
  PutStringInArray(arr, bufSringArr, i);
}

Console.WriteLine();
PrintArray(arr);

void PutStringInArray(int[,] arr, int[] mas, int indexSring)
{
  for (int j = 0; j < mas.Length;j++)
  {
    arr[indexSring, j] = mas[j];
  }
}

void SortArr(int[] mas)
{
  int buf;
  int min = 100;
  for (int i = 0; i < mas.Length-1; i++)
  {

    if (mas[mas.Length - 1] == min) return;
    if (mas[i] < min) min = mas[i];
    if (mas[i + 1] > mas[i])
    {
      buf = mas[i + 1];
      mas[i + 1] = mas[1];
      mas[1] = buf;
    }
    
  }
}

int[] GetStringArray(int[,] arr, int indexSring)
{
  int[] stringArr = new int[arr.GetLength(1)];
  for (int j = 0; j < stringArr.Length; j++)
  {
    stringArr[j] = arr[indexSring, j];
  }
  return stringArr;
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

    for (int j = 0; j < arr.GetLength(1); j++)
    {
      Console.Write(String.Format("{0,3}", arr[i, j]), " ");

    }
    Console.Write("\n");
  }
  Console.Write("\n");
}