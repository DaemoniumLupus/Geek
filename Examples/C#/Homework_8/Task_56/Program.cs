int[,] arr = new int[10, 5];
int[] bufStringArr = new int[arr.GetLength(1)];
int minSum = int.MaxValue;
int indexStringMinSum = 0;
int bufSum;

arr = GetArray(arr);
for (int i = 0; i < arr.GetLength(0); i++)
{
  bufStringArr = GetStringArray(arr, i);
  bufSum = SumString(bufStringArr);
  
  if (bufSum < minSum)
  {
    minSum = bufSum;
    indexStringMinSum = i;
  }


}

PrintArray(arr);
Console.WriteLine($"{indexStringMinSum + 1} строка имеет минимальную сумму");


int SumString(int[] stringArray)
{
  int sum = 0;
  for (int i = 0; i < stringArray.Length; i++)
  {
    sum += stringArray[i];
  }
  return sum;
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