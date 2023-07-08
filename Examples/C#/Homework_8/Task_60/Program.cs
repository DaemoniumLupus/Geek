

using System.Collections.Specialized;
using System.Reflection.Metadata.Ecma335;
using System.ComponentModel;
using System.Collections.Generic;
using System;
int[,,] arr = new int[3, 3, 3];
List<int> listUseNumber = new List<int>();
arr = GetArray(arr, listUseNumber);
PrintArray(arr);







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

int[,,] GetArray(int[,,] arr, List<int> list)
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

int NewNonRepeatingNumber(List<int> list)
{
  int num = 0;
  bool repeat = true;
  while (repeat)
  {
    num = new Random().Next(10, 100);
    repeat = false;
    for (int i = 0; i < list.Count; i++)
    {
      if (num == list[i])
      {
        repeat = true;
        break;
      }
    }
  }
  list.Add(num);
  return num;
}

