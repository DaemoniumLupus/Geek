Console.Clear();
int a = GetNumberFromUser("Введите количество чисел в массиве: ", "Ошибка ввода!");

int[] mas = new int[a];

GetArray(mas);

int res = 0;

res = GetCountEvenNumbers(res, mas);

WriteRes(mas, res);



void WriteRes(int[] mas, int res)
{
  Console.Write("[");
  for (int i = 0; i < mas.Length; i++){
    if (i+1 == mas.Length){
      Console.Write($"{mas[i]}]");
    }else{
      Console.Write($"{mas[i]}, ");
    }
  }
  Console.Write($" -> {res}");
}

int GetCountEvenNumbers(int res, int[] arr)
{
  int count = 0;
  for (int i = 0; i < arr.Length; i++)
  {
    if (arr[i] % 2 == 0)
    {
      count++;
    }
  }
  return count;
}

void GetArray(int[] arr)
{
  for (int i = 0; i < arr.Length; i++)
  {
    arr[i] = new Random().Next(100, 1000);
  }
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