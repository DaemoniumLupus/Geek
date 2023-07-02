int[,] arr = new int[10, 10];
arr = GetArray(arr);
Console.Write("Введите индекс ячейки в виде двухзначного числа: ");
int pos = GetNumberFromUser("Ошибка ввода!");
int i, j;

i = pos / 10;
j = pos % 10;

if (i < arr.GetLength(0) || j < arr.GetLength(1))
{
  Console.WriteLine($"{pos} -> {arr[i, j]}");
}
else
{
  Console.WriteLine($"{pos} -> Такого числа в массиве нет!");
}
PrintArray(arr);


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

int GetNumberFromUser(/* string message,  */string errorMessage)
{
  while (true)
  {
    //Console.Write(message);
    if (int.TryParse(Console.ReadLine(), out int userNumber))
    {
      return userNumber;
    }
    Console.WriteLine(errorMessage);
  }
}