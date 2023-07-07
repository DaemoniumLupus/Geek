int[,,] arr = new int[3, 3, 3];
int[] listNum = new int[1];
arr = GetArray(arr, listNum);
PrintArray(arr);
Console.WriteLine(string.Join(" ", listNum));





void PrintArray(int[,,] arr)
{
  for (int i = 0; i < arr.GetLength(0); i++)
  {
    for (int j = 0; j < arr.GetLength(1); j++)
    {
      for (int k = 0; k < arr.GetLength(2); k++)
      {
        Console.WriteLine($"{arr[i, j, k]} ({i},{j},{k})");
      }
    }
  }
}

int[,,] GetArray(int[,,] arr, int[] list)
{
  for (int i = 0; i < arr.GetLength(0); i++)
  {
    for (int j = 0; j < arr.GetLength(1); j++)
    {
      for (int k = 0; k < arr.GetLength(2); k++)
      {
        arr[i, j, k] = NewNonRepeatingNumber(list);
      }
    }
  }
  return arr;
}

int NewNonRepeatingNumber(int[] list)
{
  int num = 0;
  bool repeat = true;
  while (repeat)
  {
    num = new Random().Next(10, 100);
    repeat = false;
    for (int i = 0; i < list.Length; i++)
    {
      if (num == list[i])
      {
        repeat = true;
        break;
      }
    }
  }
  
  return num;
}

int[] NewList(int num, int[] list)
{
  int[] largerList = new int[list.Length + 1];
  for (int i = 0; i < list.Length; i++)
  {
    largerList[i] = list[i];
  }
  largerList[largerList.Length - 1] = num;
  return largerList;
}